from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt
from constants import *

def create_section(bg_color, label_text=None):
    section = QWidget()
    section.setStyleSheet(f"background-color: {bg_color};")
    layout = QVBoxLayout(section)
    
    if label_text:
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
    
    return section, layout

def create_separator(orientation="horizontal", color="black"):
    if orientation.lower() == "horizontal":
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
    else:  # vertical
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
    
    separator.setFrameShadow(QFrame.Sunken)
    #separator.setStyleSheet(f"color: {color};")  # This line can be removed when development is complete
    
    return separator