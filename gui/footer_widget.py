from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from constants import *
from ui_components import create_section, create_separator
from course_carousel import CourseCarousel

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
        home_section, home_layout = create_section("rgba(255, 255, 255, 0.1)")
        home_section.setFixedWidth(HOME_SECTION_WIDTH)
        home_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout.addWidget(home_section)

        # Icon
        home_icon = QLabel()
        home_icon.setPixmap(QPixmap(r"assets\icons\home.svg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        home_icon.setAlignment(Qt.AlignCenter)
        home_icon.setCursor(QCursor(Qt.PointingHandCursor))
        home_layout.setAlignment(Qt.AlignCenter)
        home_layout.addWidget(home_icon)
        
        # Course Section
        course_section, course_layout = create_section("rgba(255, 255, 255, 0.2)")
        course_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
        # Configure the course layout for maximum carousel space
        course_layout.setContentsMargins(0, 0, 0, 0)
        course_layout.setSpacing(0)
        course_layout.setAlignment(Qt.AlignCenter) 
    
        # Create carousel and make it take up the entire space
        self.carousel = CourseCarousel()
        self.carousel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.carousel.setMinimumSize(1760, 63)  # Set the desired size
        course_layout.addWidget(self.carousel)

        layout.addWidget(course_section)
        
        # Next Section
        next_section, next_layout = create_section("rgba(255, 255, 255, 0.1)")
        next_section.setFixedWidth(NEXT_SECTION_WIDTH)
        next_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # Create a vertical layout to hold both icons
        nav_layout = QHBoxLayout()
        nav_layout.setAlignment(Qt.AlignCenter)
        nav_layout.setSpacing(10)  # space between buttons

        # Scroll Left Icon
        left_icon = QLabel()
        left_icon.setPixmap(QPixmap(r"assets\icons\navigate_before.svg").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_icon.setCursor(QCursor(Qt.PointingHandCursor))
        left_icon.mousePressEvent = self.scroll_left

        # Scroll Right Icon
        right_icon = QLabel()
        right_icon.setPixmap(QPixmap(r"assets\icons\navigate_next.svg").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        right_icon.setCursor(QCursor(Qt.PointingHandCursor))
        right_icon.mousePressEvent = self.scroll_right

        # Add icons to the nav layout
        nav_layout.addWidget(left_icon)
        nav_layout.addWidget(right_icon)

        # Add nav layout to the next section
        next_layout.addLayout(nav_layout)

        # Add the final section to the main layout
        layout.addWidget(next_section)

    def scroll_right(self, _):
        if hasattr(self, 'carousel'):
            self.carousel.scroll_right()

    def scroll_left(self, _):
        if hasattr(self, 'carousel'):
            self.carousel.scroll_left()
