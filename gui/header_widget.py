from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from constants import *
from ui_components import create_section, create_separator

class HeaderWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        self.setFixedHeight(HEADER_HEIGHT)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(f"background-color: {MID_TEAL};")
        
        # Main layout for header
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Left Section
        left_section, _ = create_section("rgba(255, 255, 255, 0.1)", "LEFT_SECTION")
        left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(left_section, HEADER_LEFT_PROPORTION)
        
        # Separator
        layout.addWidget(create_separator("vertical", "white"))
        
        # Middle Section
        middle_section, _ = create_section("rgba(255, 255, 255, 0.2)", "MIDDLE_SECTION")
        middle_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(middle_section, HEADER_MIDDLE_PROPORTION)
        
        # Separator
        layout.addWidget(create_separator("vertical", "white"))
        
        # Right Section
        right_section, _ = create_section("rgba(255, 255, 255, 0.1)", "RIGHT_SECTION")
        right_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(right_section, HEADER_RIGHT_PROPORTION)