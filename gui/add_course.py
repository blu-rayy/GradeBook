import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# remove from to after debugging

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGraphicsDropShadowEffect, QSizePolicy
from PyQt5.QtGui import QColor, QPainterPath, QRegion
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
import sqlite3
from load_utils import apply_stylesheet

class AddCourse(QDialog):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        
        self.dragging = False
        self.offset = None
        self.ui_config = ui_config
        
        self.setWindowTitle("Add New Course")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(1095, 432)

        if parent:
            self.overlay = QWidget(parent)
            self.overlay.setGeometry(parent.rect())
            self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
            self.overlay.show()
        
        self.init_ui()
        self.setup_animation()
       
    def init_ui(self):
        apply_stylesheet(self, "assets/css/add_course.css")
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Main container with shadow
        main_container = QWidget()
        main_container.setObjectName("main_container")
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
        title_section.setStyleSheet("background-color: #186060;")

        title_layout = QHBoxLayout(title_section)
        title_layout.setContentsMargins(15, 0, 15, 0)
        title_label = QLabel("Add New Course")
        title_label.setObjectName("title_label")
        title_label.setAlignment(Qt.AlignCenter)

        close_button = QPushButton("✕")
        close_button.setFixedSize(24, 24)
        close_button.setCursor(Qt.PointingHandCursor)
        close_button.setObjectName("close_button")
        close_button.clicked.connect(self.close)

        # Add widgets to layout
        title_layout.addWidget(title_label)
        title_layout.addWidget(close_button, Qt.AlignRight)

        container_layout.addWidget(title_section)
                
        # Content section
        content_section = QWidget()
        content_section.setObjectName("content_section")
        content_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        content_layout = QVBoxLayout(content_section)
        content_layout.setContentsMargins(43, 43, 43, 43)
        content_layout.setSpacing(14)
        
        # First row - Course Title
        title_row = QWidget()
        title_row_layout = QVBoxLayout(title_row)
        title_row_layout.setContentsMargins(0, 0, 0, 0)
        title_row_layout.setSpacing(5)

        input_group = QWidget()
        input_group_layout = QHBoxLayout(input_group)
        input_group_layout.setContentsMargins(0, 0, 0, 0)
        input_group_layout.setSpacing(0)
        
        prefix_label = QLabel("Course Title")
        prefix_label.setObjectName("title_input_prefix")
        prefix_label.setFixedHeight(40)
        prefix_label.setFixedWidth(110)
        prefix_label.setAlignment(Qt.AlignCenter)
        
        self.title_input = QLineEdit()
        self.title_input.setFixedHeight(40)
        self.title_input.setObjectName("title_input")
        self.title_input.setPlaceholderText("e.g., Introduction to Computing (LEC)")

        input_group_layout.addWidget(prefix_label)
        input_group_layout.addWidget(self.title_input)
        
        title_row_layout.addWidget(input_group)
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
        #import_button.setObjectName("bottom_button")
        import_button.setStyleSheet(f"""
           QPushButton {{
                background-color: {self.ui_config['colors']['MID_TEAL']};
                border: none;
                border-radius: 20px;
                color: {self.ui_config['colors']['SNOW_WHITE']};
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 15px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.ui_config['colors']['DARK_TEAL']};
            }}
        """)
        import_button.clicked.connect(self.import_course)
        
        create_button = QPushButton("Create Course")
        create_button.setFixedSize(170, 40)
        create_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.ui_config['colors']['MID_TEAL']};
                border: none;
                border-radius: 20px;
                color: {self.ui_config['colors']['SNOW_WHITE']};
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 15px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.ui_config['colors']['DARK_TEAL']};
            }}
        """)
        create_button.setObjectName("create_button")
        create_button.clicked.connect(self.create_course)
        
        button_layout.addWidget(import_button)
        button_layout.addWidget(create_button)
        content_layout.addWidget(button_row)
        
        container_layout.addWidget(content_section)
        main_layout.addWidget(main_container)

    def closeEvent(self, event):
        if hasattr(self, 'overlay') and self.overlay:
            self.overlay.hide()
            self.overlay.deleteLater()
        super().closeEvent(event)
        
    def setup_animation(self):
        """Setup the popup animation"""
        # Get screen or parent dimensions for positioning
        screen_width = self.parent().width() if self.parent() else self.screen().size().width()
        screen_height = self.parent().height() if self.parent() else self.screen().size().height()
    
    # Calculate center position
        center_x = screen_width // 2 - self.width() // 2
    
    # Set initial position below the screen (for slide up animation)
        self.move(center_x, screen_height)
    
    # Create animation to slide up from bottom to center
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setEndValue(QPoint(center_x, screen_height // 2 - self.height() // 2))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
    
        if hasattr(self, 'overlay') and self.overlay and self.parent():
            self.overlay.setGeometry(self.parent().rect())
        # fade in animation
            self.overlay_animation = QPropertyAnimation(self.overlay, b"windowOpacity")
            self.overlay_animation.setDuration(300)
            self.overlay_animation.setStartValue(0.0)
            self.overlay_animation.setEndValue(1.0)
            self.overlay_animation.setEasingCurve(QEasingCurve.OutCubic)
            self.overlay.setWindowOpacity(0.0)
        
    def showEvent(self, event):
        """Override show event to start animation"""
        super().showEvent(event)
        self.animation.start()

        # Start overlay animation if it exists
        if hasattr(self, 'overlay_animation'):
            self.overlay_animation.start()
        
    def mousePressEvent(self, event):
        """Handle mouse press events"""
        # Check if we're clicking on the title section
        pos = event.pos()
        widget_under_cursor = self.childAt(pos)
    
        # If we clicked on the title section or its children
        title_section_rect = self.findChild(QWidget, "title_section").geometry()
        if title_section_rect.contains(pos) and not isinstance(widget_under_cursor, QPushButton):
            self.dragging = True
            self.offset = event.pos()
        # Close if clicking outside the dialog content
        elif not self.childAt(pos):
            self.close()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Handle mouse movement"""
        if self.dragging and self.offset:
            new_pos = self.mapToGlobal(event.pos() - self.offset)
            self.move(new_pos)
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release"""
        self.dragging = False
        super().mouseReleaseEvent(event)
    
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

    def apply_rounded_mask(self):
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 30, 30)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)


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