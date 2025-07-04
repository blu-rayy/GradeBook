from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QPushButton, QSizePolicy, QFrame
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt5.QtGui import QFont
from load_utils import *
import sqlite3

class CourseCarousel(QWidget):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        self.ui_config = ui_config
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.scroll = QScrollArea()
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setAlignment(Qt.AlignLeft)
        self.scroll.setFrameShape(QFrame.NoFrame) 
        self.scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        container = QWidget()
        container.setFixedHeight(63)
        container.setStyleSheet("background: transparent; border: none;")

        self.courses_layout = QHBoxLayout(container)
        self.courses_layout.setContentsMargins(0, 0, 0, 0)
        self.courses_layout.setSpacing(0)
        self.courses_layout.setAlignment(Qt.AlignLeft)

        #course_names = self.fetch_course_nicknames()
        course_names = [
             "TECHNO CCS103", "APPDEV CS43", "PYTHON CS48",
             "PDCOM CS51", "AUTOMATA CS23", "ML CS98", "DBSYS CS33"
            ]

        for course in course_names:
            print(f"Creating button for: {course}")
            btn = self.create_course_box(course) #debugging line
            self.courses_layout.addWidget(btn)
            print(f"Button created: {btn}") #debugging line

        self.scroll.setWidget(container)
        self.layout.addWidget(self.scroll)
        
        # Setup animation
        self.scroll_animation = QPropertyAnimation(self.scroll.horizontalScrollBar(), b"value")
        self.scroll_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.scroll_animation.setDuration(300) 

    def fetch_course_nicknames(self):
        course_nicknames = ["TECHNO CCS103"]
        try:
            conn = sqlite3.connect('db/gradebook.db')
            cursor = conn.cursor()
            
            cursor.execute("SELECT course_nickname, course_code FROM course ORDER BY courseID")
            
            results = cursor.fetchall()
            
            # Format as "NICKNAME CODE" 
            for nickname, code in results:
                course_nicknames.append(f"{nickname} {code}")
                
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}. Using placeholder values...")
        except Exception as e:
            print(f"Error fetching course nicknames: {e} Using placeholder values...")
            
        return course_nicknames
    
    def create_course_box(self, name):
        btn = QPushButton(name)
        btn.setFixedSize(320, 63)
        
        font_name = self.ui_config["fonts"]["HEADING_FONT_MEDIUM"]
        btn.setFont(QFont(font_name, 16))
        
        btn.setStyleSheet(load_stylesheet("assets\css\course_carousel_button.css"))

        btn.setProperty("alignment", Qt.AlignLeft)
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