#  ImageTranslator

ImageTranslator es una aplicación de escritorio construida con **Python** y **PyQt5** que permite extraer texto de imágenes del portapapeles mediante OCR (Tesseract) y traducirlo instantáneamente a múltiples idiomas usando Google Translate.

Descargar última versión aquí:

https://github.com/Corbatin/ImageTranslator/releases

##  Características
- **Pegado directo:** Captura imágenes directamente desde tu portapapeles.
- **OCR:** Extracción de texto precisa a través de Tesseract.
- **Traducción Multilingüe:** Soporte para decenas de idiomas con `deep-translator`.
- **Interfaz Moderna:** Diseño oscuro (Dark Mode) estilizado con QSS.

## Requisitos Previos

Antes de instalar las librerías de Python, **debes instalar Tesseract OCR** en tu sistema:

1. **Windows:** - Descarga el instalador desde [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Asegúrate de instalarlo en la ruta por defecto: `C:\Program Files\Tesseract-OCR\`.
2. **Linux (Ubuntu/Debian):**
   - `sudo apt update`
   - `sudo apt install tesseract-ocr`
3. **macOS:**
   - `brew install tesseract`
   
##  Instalación

1. **Clona el repositorio:**
   ```bash
   git clone (https://github.com/Corbatin/ImageTranslator.git)
   cd ImageTranslator

2. **Crea un entorno virtual (recomendado)**:

```Bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Linux/Mac:
    source venv/bin/activate
```
3. **Instala las dependencias**:

 ```Bash
    pip install -r requirements.txt
 ```
4. **Uso**

Ejecutar la aplicación:
- `python main.py`
