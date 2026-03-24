"""
ImageTranslator - Aplicación de OCR y Traducción
Punto de entrada de la aplicación
"""

import sys
from PyQt5.QtWidgets import QApplication
from ui import ClipboardImageApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClipboardImageApp()
    window.show()
    sys.exit(app.exec_())