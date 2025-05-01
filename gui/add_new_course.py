import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# remove from to after debugging

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGraphicsDropShadowEffect, QSizePolicy
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
import sqlite3
from load_utils import apply_stylesheet

class AddCourse(QDialog):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        
        # Load UI configuration
        self.ui_config = ui_config
        
        # Set window properties
        self.setWindowTitle("Add New Course")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(1095, 432)
        
        self.init_ui()
        self.setup_animation()
       
    def init_ui(self):
        apply_stylesheet(self, "assets/css/add_course.css")
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Main container with shadow
        main_container = QWidget()
        container_layout = QVBoxLayout(main_container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        
        # Add shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 80))
        main_container.setGraphicsEffect(shadow)
        
        # Title section
        title_section = QWidget()
        title_section.setObjectName("title_section")
        title_section.setFixedHeight(60)
        title_section.setStyleSheet("background-color: #186060;")  # Match the teal background

        title_layout = QHBoxLayout(title_section)
        title_label = QLabel("Add New Course")
        title_label.setObjectName("title_label")
        title_label.setAlignment(Qt.AlignCenter)

        close_button = QPushButton("✕")
        close_button.setFixedSize(24, 24)
        close_button.setCursor(Qt.PointingHandCursor)
        close_button.setObjectName("close_button")
        close_button.clicked.connect(self.close)

        # Add widgets to layout
        title_layout.addStretch(1)  # Add stretch on the left
        title_layout.addWidget(title_label, 4)
        #title_layout.addWidget(close_button, 0, Qt.AlignRight | Qt.AlignVCenter)

        container_layout.addWidget(title_section)
                
        # Content section
        content_section = QWidget()
        content_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        content_section.setStyleSheet("background-color: white; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;")
        
        content_layout = QVBoxLayout(content_section)
        content_layout.setContentsMargins(43, 43, 43, 43)
        content_layout.setSpacing(14)
        
        # First row - Course Title
        title_row = QWidget()
        title_row_layout = QVBoxLayout(title_row)
        title_row_layout.setContentsMargins(0, 0, 0, 0)
        title_row_layout.setSpacing(5)
        
        title_label = QLabel("Course Title")
        title_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 16px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.title_input = QLineEdit()
        self.title_input.setFixedHeight(40)
        self.title_input.setPlaceholderText("e.g., Introduction to Computing (LEC)")
        self.title_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 14px;
            }}
        """)
        
        # Add shadow to title input
        title_shadow = QGraphicsDropShadowEffect()
        title_shadow.setBlurRadius(5)
        title_shadow.setOffset(0, 2)
        title_shadow.setColor(QColor(0, 0, 0, 30))
        self.title_input.setGraphicsEffect(title_shadow)
        
        title_row_layout.addWidget(title_label)
        title_row_layout.addWidget(self.title_input)
        content_layout.addWidget(title_row)
        
        # Placeholder for future rows
        # (We'll add more input fields in subsequent steps)
        
        # Button row
        button_row = QWidget()
        button_layout = QHBoxLayout(button_row)
        button_layout.setContentsMargins(0, 20, 0, 0)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(20)
        
        import_button = QPushButton("Import Course")
        import_button.setFixedSize(170, 40)
        import_button.setStyleSheet(f"""
            QPushButton {{
                background-color: white;
                border: 2px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                color: {self.ui_config['colors']['MID_TEAL']};
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #F0F0F0;
            }}
        """)
        import_button.clicked.connect(self.import_course)
        
        create_button = QPushButton("Create Course")
        create_button.setFixedSize(170, 40)
        create_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.ui_config['colors']['MID_TEAL']};
                border: none;
                border-radius: 5px;
                color: white;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.ui_config['colors']['DARK_TEAL']};
            }}
        """)
        create_button.clicked.connect(self.create_course)
        
        button_layout.addWidget(import_button)
        button_layout.addWidget(create_button)
        content_layout.addWidget(button_row)
        
        container_layout.addWidget(content_section)
        main_layout.addWidget(main_container)
        
        # Semi-transparent background
        self.setStyleSheet("background-color: rgba(0, 0, 0, 80);")
        
    def setup_animation(self):
        """Setup the popup animation"""
        # Set initial position below the screen
        self.move(
            (self.parent().width() if self.parent() else self.screen().size().width()) // 2 - self.width() // 2,
            (self.parent().height() if self.parent() else self.screen().size().height())
        )
        
        # Create animation
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setEndValue(QPoint(
            (self.parent().width() if self.parent() else self.screen().size().width()) // 2 - self.width() // 2,
            (self.parent().height() if self.parent() else self.screen().size().height()) // 2 - self.height() // 2
        ))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
    def showEvent(self, event):
        """Override show event to start animation"""
        super().showEvent(event)
        self.animation.start()
        
    def mousePressEvent(self, event):
        """Handle mouse press events"""
        # Close the dialog if clicking outside the main content area
        if not self.childAt(event.pos()):
            self.close()
        super().mousePressEvent(event)
    
    def import_course(self):
        """Handle import course button click"""
        print("Clicked Import Course")
        
    def create_course(self):
        """Handle create course button click and database insertion"""
        print("Clicked Create Course")
        
        # Get values from input fields
        course_title = self.title_input.text()
        
        # Basic validation - just for the title for now
        if not course_title:
            print("Course title must be filled!")
            return
            
        try:
            # Connect to database
            conn = sqlite3.connect('db/gradebook.db')
            cursor = conn.cursor()
            
            # For now, we'll just insert a placeholder row with the title
            # We'll expand this in subsequent steps
            cursor.execute("""
                INSERT INTO course (course_title, course_nickname, course_code, units, section, linked_courseID)
                VALUES (?, ?, ?, ?, ?, NULL)
            """, (course_title, "Placeholder", "PLCH101", 3, "TN01"))
            
            lec_course_id = cursor.lastrowid
            
            conn.commit()
            conn.close()
            
            print(f"Course created successfully! ID: {lec_course_id}")
            self.accept()  # Close dialog on success
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    #remove after debugging
    import json

    # remove after debugging
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "ui_config.json"), "r") as f:
        ui_config = json.load(f)
    #remove after debugging
    
    app = QApplication(sys.argv)
    #uncomment below after debugging
    #dialog = AddCourse()
    dialog = AddCourse(ui_config=ui_config) #remove after debugging
    dialog.show()
    
    sys.exit(app.exec_())