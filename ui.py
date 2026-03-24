"""
Interfaz gráfica de la aplicación ImageTranslator
Construye y gestiona los widgets
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
                             QPushButton, QLabel, QMessageBox, QFrame, QComboBox, QTextEdit, QApplication)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from styles import (MAIN_STYLESHEET, RIGHT_PANEL_STYLESHEET, TITLE_STYLESHEET,
                    LABEL_TRANSPARENT, LINE_SEPARATOR_STYLESHEET, IMAGE_LABEL_LOADED)
from logic import extract_text_from_pixmap, translate_text, get_supported_languages


class ClipboardImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Imagen y Traductor")
        self.resize(1100, 650)
        self.setStyleSheet(MAIN_STYLESHEET)
        
        self._build_ui()

    def _build_ui(self):
        """Construye la interfaz gráfica completa"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header superior
        top_panel = self._build_top_panel()
        main_layout.addWidget(top_panel)

        # Contenido principal (izquierda y derecha)
        content_layout = QHBoxLayout()
        left_container = self._build_left_panel()
        right_panel = self._build_right_panel()
        
        content_layout.addLayout(left_container, stretch=1)
        content_layout.addWidget(right_panel, stretch=1)
        
        main_layout.addLayout(content_layout, stretch=1)

    def _build_top_panel(self):
        """Construye el panel superior (título y barra de menú)"""
        top_frame = QFrame()
        top_frame.setStyleSheet("background-color: #1a1a1a; border-bottom: 1px solid #00a4ef;")
        top_frame.setFixedHeight(70)
        
        top_layout = QHBoxLayout(top_frame)
        top_layout.setContentsMargins(15, 10, 15, 10)
        
        # Título principal
        titulo = QLabel("ImageTranslator")
        titulo_font = QFont('Segoe UI', 16, QFont.Bold)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #00a4ef; border: none; background: transparent;")
        
        top_layout.addWidget(titulo)
        top_layout.addStretch()
        
        # Botones de menú
        help_btn = QPushButton("Ayuda")
        help_btn.clicked.connect(self.show_help)
        help_btn.setMaximumWidth(120)
        
        about_btn = QPushButton("Acerca de")
        about_btn.clicked.connect(self.show_about)
        about_btn.setMaximumWidth(120)
        
        # Aplicar estilos a botones del header
        btn_style = """
            QPushButton {
                background-color: #00a4ef;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                color: white;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #48bcf7;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """
        
        for btn in [help_btn, about_btn]:
            btn.setStyleSheet(btn_style)
        
        top_layout.addWidget(help_btn)
  
        top_layout.addWidget(about_btn)
        
        return top_frame

    def _build_left_panel(self):
        """Construye el panel izquierdo (imagen y botón pegar)"""
        left_container = QVBoxLayout()
        
        self.image_label = QLabel("Pega una imagen aquí")
        self.image_label.setAlignment(Qt.AlignCenter)
        
        paste_btn = QPushButton("Pegar Imagen")
        paste_btn.clicked.connect(self.paste_image)
        
        left_container.addWidget(self.image_label, stretch=5)
        left_container.addWidget(paste_btn, stretch=1)
        
        return left_container

    def _build_right_panel(self):
        """Construye el panel derecho (OCR y traducción)"""
        right_panel = QFrame()
        right_panel.setStyleSheet(RIGHT_PANEL_STYLESHEET)
        right_layout = QVBoxLayout(right_panel)
        
        # Título
        titulo_derecho = QLabel("HERRAMIENTAS OCR")
        titulo_derecho.setStyleSheet(TITLE_STYLESHEET)
        titulo_derecho.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(titulo_derecho)
        
        # --- Sección de Extracción de Texto ---
        right_layout.addWidget(QLabel("Texto Extraído:", styleSheet=LABEL_TRANSPARENT))
        self.texto_extraido_txt = QTextEdit()
        self.texto_extraido_txt.setPlaceholderText("El texto detectado aparecerá aquí...")
        right_layout.addWidget(self.texto_extraido_txt)

        extraerTexto_btn = QPushButton("Extraer Texto")
        extraerTexto_btn.clicked.connect(self.extract_text_logic)
        right_layout.addWidget(extraerTexto_btn)

        # Separador visual
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(LINE_SEPARATOR_STYLESHEET)
        right_layout.addWidget(line)

        # --- Sección de Traducción ---
        right_layout.addWidget(QLabel("Traducción:", styleSheet=LABEL_TRANSPARENT))
        
        self.idiomaDestino_chk = QComboBox()
        self.idiomaDestino_chk.addItems(get_supported_languages())
        right_layout.addWidget(self.idiomaDestino_chk)

        self.texto_traducido_txt = QTextEdit()
        self.texto_traducido_txt.setPlaceholderText("La traducción aparecerá aquí...")
        right_layout.addWidget(self.texto_traducido_txt)

        traducir_btn = QPushButton("Traducir")
        traducir_btn.clicked.connect(self.translate_text_logic)
        right_layout.addWidget(traducir_btn)
        
        return right_panel

    def paste_image(self):
        """Pega una imagen del portapapeles en el label"""
        clipboard = QApplication.clipboard()
        if clipboard.mimeData().hasImage():
            pixmap = clipboard.pixmap()
            if not pixmap.isNull():
                # Escalado proporcional al tamaño actual del label
                scaled_pixmap = pixmap.scaled(
                    self.image_label.width(), 
                    self.image_label.height(), 
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
                self.image_label.setStyleSheet(IMAGE_LABEL_LOADED)
            else:
                QMessageBox.warning(self, "Error", "La imagen no es válida.")
        else:
            QMessageBox.information(self, "Aviso", "No hay imagen en el portapapeles.")

    def extract_text_logic(self):
        """Extrae texto de la imagen usando OCR"""
        pixmap = self.image_label.pixmap()
        if pixmap is None or pixmap.isNull():
            QMessageBox.warning(self, "Error", "No hay ninguna imagen cargada para procesar.")
            return

        try:
            text = extract_text_from_pixmap(pixmap)
            self.texto_extraido_txt.setText(text)
        except Exception as e:
            QMessageBox.critical(self, "Error de OCR", f"Hubo un fallo al extraer texto: {str(e)}")

    def translate_text_logic(self):
        """Traduce el texto extraído al idioma seleccionado"""
        texto_a_traducir = self.texto_extraido_txt.toPlainText()
        if not texto_a_traducir.strip():
            QMessageBox.warning(self, "Aviso", "No hay texto para traducir.")
            return

        idioma_nombre = self.idiomaDestino_chk.currentText().lower()
        
        try:
            resultado = translate_text(texto_a_traducir, idioma_nombre)
            self.texto_traducido_txt.setText(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo traducir: {str(e)}")

    def show_about(self):
        """Muestra información acerca de la aplicación"""
        QMessageBox.information(
            self, 
            "Acerca de ImageTranslator",
            "ImageTranslator v1.0\n\n"
            "Aplicación de OCR y traducción de imágenes\n\n"
            "Características:\n"
            "• Extracción de texto con Tesseract OCR\n"
            "• Traducción automática con Google Translator\n"
            "• Múltiples idiomas soportados\n\n"
            "Desarrollado por: Benjamín Melis\n"
        )

    def show_help(self):
        """Muestra información de ayuda"""
        QMessageBox.information(
            self,
            "Ayuda",
            "Cómo usar ImageTranslator:\n\n"
            "1. Pega una imagen desde el portapapeles\n"
            "2. Haz clic en 'Extraer Texto' para detectar el texto\n"
            "3. Selecciona el idioma de destino\n"
            "4. Haz clic en 'Traducir' para traducir el texto\n\n"
            "Notas:\n"
            "• Asegúrate de tener Tesseract OCR instalado\n"
            "• Se requiere conexión a internet para traducir"
        )

    def show_config(self):
        """Muestra opciones de configuración"""
        QMessageBox.information(
            self,
            "Configuración",
            "Opciones de configuración disponibles:\n\n"
            "• Idioma origen: Auto-detección\n"
            "• Idioma destino: Selecciona de la lista\n\n"
            "Más opciones estarán disponibles en futuras versiones."
        )
