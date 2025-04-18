from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QPushButton, QSizePolicy, QFrame
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt5.QtGui import QFont
from constants import *

class CourseCarousel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.scroll = QScrollArea()
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setAlignment(Qt.AlignCenter)
        self.scroll.setFrameShape(QFrame.NoFrame)  # Remove the frame border
        self.scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        container = QWidget()
        container.setFixedHeight(63)
        container.setStyleSheet("background: transparent; border: none;")

        self.courses_layout = QHBoxLayout(container)
        self.courses_layout.setContentsMargins(0, 0, 0, 0)
        self.courses_layout.setSpacing(0)
        self.courses_layout.setAlignment(Qt.AlignCenter)

        course_names = [
            "TECHNO CCS103", "APPDEV CS43", "PYTHON CS48",
            "PDCOM CS51", "AUTOMATA CS23", "ML CS98", "DBSYS CS33"
        ]

        for course in course_names:
            btn = self.create_course_box(course)
            self.courses_layout.addWidget(btn)

        self.scroll.setWidget(container)
        self.layout.addWidget(self.scroll)
        
        # Setup animation
        self.scroll_animation = QPropertyAnimation(self.scroll.horizontalScrollBar(), b"value")
        self.scroll_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.scroll_animation.setDuration(300) 

    def create_course_box(self, name):
        btn = QPushButton(name)
        btn.setFixedSize(320, 63)
        btn.setFont(QFont(HEADING_FONT_MEDIUM, 16))
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: white;
                color: black;
                border: none;
                padding: 0px;
                text-align: center;
            }}
            QPushButton:hover {{
                background-color: {MID_TEAL};
                color: {SNOW_WHITE};
            }}
            QPushButton:focus {{
                border: none;
                outline: none;
            }}
        """)

        btn.setProperty("alignment", Qt.AlignCenter)
        btn.setProperty("textAlignment", Qt.AlignCenter)
        btn.setContentsMargins(0, 0, 0, 0)

        return btn

    def scroll_right(self):
        current_value = self.scroll.horizontalScrollBar().value()
        
        max_value = self.scroll.horizontalScrollBar().maximum()
        target_value = min(current_value + 330, max_value)
        
        if self.scroll_animation.state() == QAbstractAnimation.Running:
            self.scroll_animation.stop()
            
        self.scroll_animation.setStartValue(current_value)
        self.scroll_animation.setEndValue(target_value)
        self.scroll_animation.start()
    
    def scroll_left(self):
        current_value = self.scroll.horizontalScrollBar().value()
        
        target_value = max(current_value - 330, 0)
        
        if self.scroll_animation.state() == QAbstractAnimation.Running:
            self.scroll_animation.stop()
            
        self.scroll_animation.setStartValue(current_value)
        self.scroll_animation.setEndValue(target_value)
        self.scroll_animation.start()