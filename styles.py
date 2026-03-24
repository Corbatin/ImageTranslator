"""
Estilos CSS para la aplicación ImageTranslator
"""

MAIN_STYLESHEET = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    QPushButton {
        background-color: #005a9e;
        border: none;
        padding: 12px;
        border-radius: 6px;
        font-weight: bold;
        color: white;
    }
    QPushButton:hover {
        background-color: #00a4ef;
        border: 1px solid #ffffff;
    }
    QPushButton:pressed {
        background-color: #48bcf7;
    }
    QLabel {
        border: 2px dashed #555;
        background-color: #333;
        border-radius: 10px;
    }
    QTextEdit {
        background-color: #1e1e1e;
        color: #dcdcdc;
        border: 1px solid #444;
        border-radius: 5px;
        font-size: 13px;
    }
    QComboBox {
        background-color: #444;
        color: white;
        border: 1px solid #666;
        padding: 5px;
    }
"""

RIGHT_PANEL_STYLESHEET = "background-color: #3c3f41; border-radius: 15px;"

TITLE_STYLESHEET = "border: none; font-size: 16px; font-weight: bold; color: #00a4ef;"

LABEL_TRANSPARENT = "border:none; background:transparent;"

LINE_SEPARATOR_STYLESHEET = "background-color: #555;"

IMAGE_LABEL_LOADED = "border: 2px solid #00a4ef; background-color: #333;"
