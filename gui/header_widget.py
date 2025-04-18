from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from constants import *
from ui_components import create_section

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
        left_section, left_layout = create_section(MID_TEAL)
        left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        left_inner_layout = QHBoxLayout()
        left_inner_layout.setContentsMargins(10, 0, 0, 0)
        left_inner_layout.setSpacing(10)

        # Icon
        calendar_icon = QLabel()
        calendar_icon.setPixmap(QPixmap("assets\icons\calendar.svg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        calendar_icon.setFixedSize(24, 24)

        # Text
        term_label = QLabel("2nd Year – Third Trimester")
        term_label.setFont(QFont(HEADING_FONT, 14))
        term_label.setStyleSheet(f"color: {SNOW_WHITE}")

        left_inner_layout.addWidget(calendar_icon)
        left_inner_layout.addWidget(term_label)
        left_inner_layout.addStretch()

        left_layout.addLayout(left_inner_layout)
        layout.addWidget(left_section, HEADER_LEFT_PROPORTION)
        
        # Middle Section
        middle_section, _ = create_section(MID_TEAL)
        middle_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(middle_section, HEADER_MIDDLE_PROPORTION)

        # Label Placeholder
        logo_label = QLabel("LOGO")
        logo_label.setAlignment(Qt.AlignCenter)  
        logo_label.setFont(QFont(HEADING_FONT_EXTRABOLD, 20))
        logo_label.setStyleSheet(f"color: {SNOW_WHITE};")
        middle_section.layout().setContentsMargins(50, 0, 50, 0)
        middle_section.layout().addWidget(logo_label)
        layout.addWidget(middle_section, HEADER_MIDDLE_PROPORTION)

        #Right Section
        right_section, right_layout = create_section(MID_TEAL)
        right_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        right_inner_layout = QHBoxLayout()
        right_inner_layout.setContentsMargins(0, 0, 10, 0)
        right_inner_layout.setSpacing(10)
        right_inner_layout.addStretch()

        # Profile image
        profile_pic = QLabel()
        profile_pic.setPixmap(QPixmap("assets\icons\profile.png").scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        profile_pic.setFixedSize(32, 32)
        profile_pic.setStyleSheet("border-radius: 16px;")

        # Name label
        name_label = QLabel("Kristian David")
        name_label.setFont(QFont(HEADING_FONT, 14))
        name_label.setStyleSheet(f"color: {SNOW_WHITE}")

        right_inner_layout.addWidget(profile_pic)
        right_inner_layout.addWidget(name_label)

        right_layout.addLayout(right_inner_layout)
        layout.addWidget(right_section, HEADER_RIGHT_PROPORTION)
