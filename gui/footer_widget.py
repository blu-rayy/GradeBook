from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor

from load_utils import *
from gui.ui_components import create_section
from gui.course_carousel import CourseCarousel

class FooterWidget(QWidget):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        self.ui_config = ui_config
        self.init_ui()
        
    def init_ui(self):
        apply_stylesheet(self, r"assets\css\footer_widget.css")
        self.setFixedHeight(self.ui_config["dimensions"]["FOOTER_HEIGHT"])
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        # Main layout for footer
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Home Section
        home_section, home_layout = create_section(self.ui_config["colors"]["WHITE"])
        home_section.setFixedWidth(self.ui_config["dimensions"]["HOME_SECTION_WIDTH"])
        home_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout.addWidget(home_section)

        # Icon
        home_icon = QLabel()
        home_icon.setPixmap(QPixmap(r"assets\icons\home.svg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        home_icon.setAlignment(Qt.AlignCenter)
        home_icon.setCursor(QCursor(Qt.PointingHandCursor))
        home_icon.mousePressEvent = self.go_to_home_page
        home_layout.setAlignment(Qt.AlignCenter)
        home_layout.addWidget(home_icon)
        
        # Course Section
        course_section, course_layout = create_section(self.ui_config["colors"]["WHITE"])
        course_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Coure Carousel
        course_layout.setContentsMargins(0, 0, 0, 0)
        course_layout.setSpacing(0)
        course_layout.setAlignment(Qt.AlignCenter) 
        self.carousel = CourseCarousel(ui_config=self.ui_config)
        self.carousel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.carousel.setMinimumSize(1760, 63)  #course carousel size 
        self.carousel.setStyleSheet("border: 2px solid red;")  # Apply border to carousel instead
        course_section.setStyleSheet("background-color: white; border: 2px solid blue;")  # Debug course section
        
        course_layout.addWidget(self.carousel)

        layout.addWidget(course_section)
        
        # Next Section
        next_section, next_layout = create_section(self.ui_config["colors"]["WHITE"])
        next_section.setFixedWidth(self.ui_config["dimensions"]["NEXT_SECTION_WIDTH"])
        next_section.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        nav_layout = QHBoxLayout()
        nav_layout.setAlignment(Qt.AlignCenter)
        nav_layout.setSpacing(10)  
        
        # Scroll Left Icon
        left_icon = QLabel()
        left_icon.setPixmap(QPixmap(r"assets\icons\navigate_before.svg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_icon.setCursor(QCursor(Qt.PointingHandCursor))
        left_icon.mousePressEvent = self.scroll_left

        # Scroll Right Icon
        right_icon = QLabel()
        right_icon.setPixmap(QPixmap(r"assets\icons\navigate_next.svg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        right_icon.setCursor(QCursor(Qt.PointingHandCursor))
        right_icon.mousePressEvent = self.scroll_right

        nav_layout.addWidget(left_icon)
        nav_layout.addWidget(right_icon)
        next_layout.addLayout(nav_layout)
        layout.addWidget(next_section)

    def scroll_right(self, _):
        if hasattr(self, 'carousel'):
            self.carousel.scroll_right()

    def scroll_left(self, _):
        if hasattr(self, 'carousel'):
            self.carousel.scroll_left()

    def go_to_home_page(self, event):
        # find the main window (parent of parent)
        main_window = self.window()
    
        # remove current widget (body)
        if hasattr(main_window, 'body'):
            main_window.main_layout.removeWidget(main_window.body)
            main_window.body.deleteLater()
    
        # create new body widget (home)
        from gui.home_body_widget import HomeBodyWidget
        main_window.body = HomeBodyWidget(ui_config=self.ui_config)
        main_window.main_layout.insertWidget(1, main_window.body)
