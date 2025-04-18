from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from constants import *
from ui_components import create_section, create_separator

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        self.setFixedHeight(FOOTER_HEIGHT)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(f"background-color: {DARK_TEAL};")
        
        # Main layout for footer
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Home Section
        home_section, _ = create_section("rgba(255, 255, 255, 0.1)", "HOME")
        home_section.setFixedWidth(HOME_SECTION_WIDTH)
        home_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout.addWidget(home_section)
        
        # Separator
        layout.addWidget(create_separator("vertical", "white"))
        
        # Course Section
        course_section, _ = create_section("rgba(255, 255, 255, 0.2)", "COURSE_SECTION")
        course_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(course_section)
        
        # Separator
        layout.addWidget(create_separator("vertical", "white"))
        
        # Next Section
        next_section, _ = create_section("rgba(255, 255, 255, 0.1)", "NEXT")
        next_section.setFixedWidth(NEXT_SECTION_WIDTH)
        next_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout.addWidget(next_section)