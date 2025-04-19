from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt

def create_section(bg_color, label_text=None):
    section = QWidget()
    section.setStyleSheet(f"background-color: {bg_color};")
    layout = QVBoxLayout(section)
    
    if label_text:
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
    
    return section, layout