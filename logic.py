"""
Lógica de negocio para la aplicación ImageTranslator
Incluye OCR, traducción y manejo de idiomas
"""

import pytesseract
from PIL import Image
import io
from deep_translator import GoogleTranslator
from PyQt5.QtCore import QBuffer, QIODevice
import os
import sys

# Configurar ruta de Tesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def resource_path(relative_path):
    """ Obtiene la ruta absoluta para recursos, compatible con PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Y configuras Tesseract apuntando a la carpeta incluida
pytesseract.pytesseract.tesseract_cmd = resource_path(r'Tesseract-OCR\tesseract.exe')

def extract_text_from_pixmap(pixmap):
    """
    Extrae texto de un QPixmap usando OCR (Tesseract)
    
    Args:
        pixmap: QPixmap con la imagen
        
    Returns:
        str: Texto extraído de la imagen
        
    Raises:
        Exception: Si hay error durante el OCR
    """
    # 1. Usar QBuffer de PyQt5 para capturar los datos del Pixmap
    buffer = QBuffer()
    buffer.open(QIODevice.ReadWrite)
    pixmap.save(buffer, "PNG")
    
    # 2. Pasar esos datos a PIL (usando io.BytesIO para el puente)
    image_data = io.BytesIO(buffer.data())
    img_pil = Image.open(image_data)

    # 3. Procesar con Tesseract
    text = pytesseract.image_to_string(img_pil)
    
    if not text.strip():
        return "No se detectó texto en la imagen."
    
    return text


def translate_text(texto, idioma_destino):
    """
    Traduce texto al idioma especificado usando Google Translator
    
    Args:
        texto (str): Texto a traducir
        idioma_destino (str): Idioma destino en minúsculas (ej: 'spanish', 'english')
        
    Returns:
        str: Texto traducido
        
    Raises:
        Exception: Si hay error durante la traducción
    """
    translator = GoogleTranslator(source='auto', target=idioma_destino)
    resultado = translator.translate(texto)
    return resultado


def get_supported_languages():
    """
    Obtiene la lista de idiomas soportados por Google Translator
    
    Returns:
        list: Lista de idiomas capitalizados y ordenados alfabéticamente
    """
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    return sorted([lang.title() for lang in langs_dict.keys()])
