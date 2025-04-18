from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel
from PyQt5.QtCore import Qt
from constants import *
from ui_components import create_section, create_separator

class BodyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(f"background-color: {SNOW_WHITE};")

    # Main layout for body
        layout = QVBoxLayout(self)
        layout.setContentsMargins(80, 0, 80, 0)
        layout.setSpacing(0)

    # Title Section
        title_section, title_layout = create_section(GREEN_TEAL)
        title_section.setFixedHeight(TITLE_SECTION_HEIGHT)
        title_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        title_content = QWidget()
        title_content_layout = QHBoxLayout(title_content)
        title_content_layout.setContentsMargins(80, 0, 80, 0)
        title_content_layout.setSpacing(0)

        title_label = QLabel("Course Name")
        title_label.setStyleSheet(f"font-family: {HEADING_FONT_BOLD}; font-size: 24px; color: {SNOW_WHITE};")
        title_label.setAlignment(Qt.AlignCenter)
        title_content_layout.addWidget(title_label)

        title_layout.addWidget(title_content)
        layout.addWidget(title_section)

    # Body Section
        padded_container = QWidget()
        padded_layout = QHBoxLayout(padded_container)
        padded_layout.setSpacing(0)
        sections_container = QWidget()
        sections_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sections_layout = QHBoxLayout(sections_container)
        sections_layout.setContentsMargins(0, 0, 0, 0)
        sections_layout.setSpacing(0)

    # CS Others Section
        cs_others, _ = create_section("rgba(20, 90, 90, 0.1)", "CS_OTHERS_SECTION")
        cs_others.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sections_layout.addWidget(cs_others, CS_OTHERS_PROPORTION)

    # CS SA Exams Section
        cs_sa_exams, _ = create_section("rgba(20, 90, 90, 0.2)", "CS_SA_EXAMS_SECTION")
        cs_sa_exams.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sections_layout.addWidget(cs_sa_exams, CS_SA_EXAMS_PROPORTION)

    # Grades Breakdown Section
        grades_breakdown, _ = create_section("rgba(20, 90, 90, 0.1)", "GRADES_BREAKDOWN_SECTION")
        grades_breakdown.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sections_layout.addWidget(grades_breakdown, GRADES_BREAKDOWN_PROPORTION)

        padded_layout.addWidget(sections_container)
        layout.addWidget(padded_container)
