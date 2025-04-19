from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from gui.ui_components import create_section

class HeaderWidget(QWidget):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        self.ui_config = ui_config
        self.init_ui()
        
    def init_ui(self):
        self.setFixedHeight(self.ui_config["dimensions"]["HEADER_HEIGHT"])
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(f"background-color: {self.ui_config['colors']['MID_TEAL']};")
        
        # Main layout for header
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Left Section
        left_section, left_layout = create_section(self.ui_config['colors']['MID_TEAL'])
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
        term_label.setFont(QFont(self.ui_config["fonts"]["HEADING_FONT"], 14))
        term_label.setStyleSheet(f"color: {self.ui_config['colors']['SNOW_WHITE']}")

        left_inner_layout.addWidget(calendar_icon)
        left_inner_layout.addWidget(term_label)
        left_inner_layout.addStretch()

        left_layout.addLayout(left_inner_layout)
        layout.addWidget(left_section, self.ui_config["dimensions"]["HEADER_LEFT_PROPORTION"])
        
        # Middle Section
        middle_section, _ = create_section(self.ui_config['colors']['MID_TEAL'])
        middle_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Label Placeholder
        logo_label = QLabel("LOGO")
        logo_label.setAlignment(Qt.AlignCenter)  
        logo_label.setFont(QFont(self.ui_config["fonts"]["HEADING_FONT_EXTRABOLD"], 20))
        logo_label.setStyleSheet(f"color: {self.ui_config['colors']['SNOW_WHITE']};")
        middle_section.layout().setContentsMargins(50, 0, 50, 0)
        middle_section.layout().addWidget(logo_label)
        layout.addWidget(middle_section, self.ui_config["dimensions"]["HEADER_MIDDLE_PROPORTION"])

        #Right Section
        right_section, right_layout = create_section(self.ui_config['colors']['MID_TEAL'])
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
        name_label.setFont(QFont(self.ui_config["fonts"]["HEADING_FONT"], 14))
        name_label.setStyleSheet(f"color: {self.ui_config['colors']['SNOW_WHITE']}")

        right_inner_layout.addWidget(profile_pic)
        right_inner_layout.addWidget(name_label)

        right_layout.addLayout(right_inner_layout)
        layout.addWidget(right_section, self.ui_config["dimensions"]["HEADER_RIGHT_PROPORTION"])
