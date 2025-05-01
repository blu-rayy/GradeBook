from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                           QSpinBox, QRadioButton, QPushButton, QWidget, QFileDialog,
                           QGraphicsDropShadowEffect, QSizePolicy)
from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QPoint, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sqlite3
import os

class AddNewCoursePopup(QDialog):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        self.ui_config = ui_config or {
            'colors': {
                'MID_TEAL': '#2C8C99',
                'DARK_TEAL': '#0A2E36',
                'SNOW_WHITE': '#FFFFFF',
                'GRAY': '#888888'
            },
            'fonts': {
                'HEADING_FONT': 'Narnoor Medium',
                'BODY_FONT': 'Inter'
            }
        }
        
        # Set window properties
        self.setWindowTitle("Add New Course")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(1095, 432)
        
        # Initialize UI
        self.init_ui()
        
        # Set animation for entry
        self.setup_animation()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Main container with shadow
        main_container = QWidget()
        container_layout = QVBoxLayout(main_container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        
        # Add shadow effect to the main container
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 80))
        main_container.setGraphicsEffect(shadow)
        
        # Title section (1095x50)
        title_section = QWidget()
        title_section.setFixedHeight(50)
        title_section.setStyleSheet(f"background-color: {self.ui_config['colors']['MID_TEAL']}; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        
        title_layout = QVBoxLayout(title_section)
        title_layout.setContentsMargins(0, 0, 0, 0)
        
        title_label = QLabel("ADD NEW COURSE")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['HEADING_FONT']}; font-size: 30px; color: {self.ui_config['colors']['SNOW_WHITE']};")
        
        title_layout.addWidget(title_label)
        container_layout.addWidget(title_section)
        
        # Content section (1013x296)
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
        
        # Second row - Nickname, Code, Section
        second_row = QWidget()
        second_row_layout = QHBoxLayout(second_row)
        second_row_layout.setContentsMargins(0, 0, 0, 0)
        second_row_layout.setSpacing(14)
        
        # Nickname section
        nickname_section = QWidget()
        nickname_layout = QVBoxLayout(nickname_section)
        nickname_layout.setContentsMargins(0, 0, 0, 0)
        nickname_layout.setSpacing(5)
        
        nickname_label = QLabel("Course Nickname")
        nickname_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 16px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.nickname_input = QLineEdit()
        self.nickname_input.setFixedHeight(40)
        self.nickname_input.setMaxLength(15)  # Limit to 15 characters
        self.nickname_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 14px;
            }}
        """)
        
        nickname_shadow = QGraphicsDropShadowEffect()
        nickname_shadow.setBlurRadius(5)
        nickname_shadow.setOffset(0, 2)
        nickname_shadow.setColor(QColor(0, 0, 0, 30))
        self.nickname_input.setGraphicsEffect(nickname_shadow)
        
        nickname_layout.addWidget(nickname_label)
        nickname_layout.addWidget(self.nickname_input)
        nickname_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        second_row_layout.addWidget(nickname_section, 481)
        
        # Course Code section
        code_section = QWidget()
        code_layout = QVBoxLayout(code_section)
        code_layout.setContentsMargins(0, 0, 0, 0)
        code_layout.setSpacing(5)
        
        code_label = QLabel("Course Code")
        code_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 16px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.code_input = QLineEdit()
        self.code_input.setFixedHeight(40)
        self.code_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 14px;
            }}
        """)
        
        code_shadow = QGraphicsDropShadowEffect()
        code_shadow.setBlurRadius(5)
        code_shadow.setOffset(0, 2)
        code_shadow.setColor(QColor(0, 0, 0, 30))
        self.code_input.setGraphicsEffect(code_shadow)
        
        code_layout.addWidget(code_label)
        code_layout.addWidget(self.code_input)
        code_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        second_row_layout.addWidget(code_section, 337)
        
        # Section section
        section_widget = QWidget()
        section_layout = QVBoxLayout(section_widget)
        section_layout.setContentsMargins(0, 0, 0, 0)
        section_layout.setSpacing(5)
        
        section_label = QLabel("Section")
        section_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 16px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.section_input = QLineEdit()
        self.section_input.setFixedHeight(40)
        self.section_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 14px;
            }}
        """)
        
        section_shadow = QGraphicsDropShadowEffect()
        section_shadow.setBlurRadius(5)
        section_shadow.setOffset(0, 2)
        section_shadow.setColor(QColor(0, 0, 0, 30))
        self.section_input.setGraphicsEffect(section_shadow)
        
        section_layout.addWidget(section_label)
        section_layout.addWidget(self.section_input)
        section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        second_row_layout.addWidget(section_widget, 166)
        
        content_layout.addWidget(second_row)
        
        # Third row - Radio button, spinners, template selection
        third_row = QWidget()
        third_row_layout = QHBoxLayout(third_row)
        third_row_layout.setContentsMargins(0, 0, 0, 0)
        third_row_layout.setSpacing(20)
        
        # Left side with radio button and spinners
        left_side = QWidget()
        left_layout = QVBoxLayout(left_side)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        
        # Radio button
        self.has_lab_radio = QRadioButton("Has Laboratory")
        self.has_lab_radio.setStyleSheet(f"""
            QRadioButton {{
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 20px;
                color: {self.ui_config['colors']['DARK_TEAL']};
            }}
            QRadioButton::indicator {{
                width: 32px;
                height: 32px;
            }}
            QRadioButton::indicator:checked {{
                background-color: {self.ui_config['colors']['MID_TEAL']};
                border: 2px solid {self.ui_config['colors']['DARK_TEAL']};
                border-radius: 16px;
            }}
            QRadioButton::indicator:unchecked {{
                border: 2px solid {self.ui_config['colors']['DARK_TEAL']};
                border-radius: 16px;
            }}
        """)
        left_layout.addWidget(self.has_lab_radio)
        
        # Spinners row
        spinners_row = QWidget()
        spinners_layout = QHBoxLayout(spinners_row)
        spinners_layout.setContentsMargins(0, 0, 0, 0)
        spinners_layout.setSpacing(10)
        
        # Lecture spinner
        lec_spinner_widget = QWidget()
        lec_spinner_layout = QVBoxLayout(lec_spinner_widget)
        lec_spinner_layout.setContentsMargins(0, 0, 0, 0)
        lec_spinner_layout.setSpacing(5)
        
        lec_label = QLabel("Lecture Units")
        lec_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 14px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.lec_spinner = QSpinBox()
        self.lec_spinner.setObjectName("LEC_SPINNER")
        self.lec_spinner.setRange(0, 5)
        self.lec_spinner.setValue(3)  # Default value
        self.lec_spinner.setFixedSize(113, 40)
        self.lec_spinner.setStyleSheet(f"""
            QSpinBox {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 16px;
            }}
            QSpinBox::up-button, QSpinBox::down-button {{
                width: 20px;
                border-left: 1px solid {self.ui_config['colors']['MID_TEAL']};
            }}
        """)
        
        lec_shadow = QGraphicsDropShadowEffect()
        lec_shadow.setBlurRadius(5)
        lec_shadow.setOffset(0, 2)
        lec_shadow.setColor(QColor(0, 0, 0, 30))
        self.lec_spinner.setGraphicsEffect(lec_shadow)
        
        lec_spinner_layout.addWidget(lec_label)
        lec_spinner_layout.addWidget(self.lec_spinner)
        spinners_layout.addWidget(lec_spinner_widget)
        
        # Lab spinner
        lab_spinner_widget = QWidget()
        lab_spinner_layout = QVBoxLayout(lab_spinner_widget)
        lab_spinner_layout.setContentsMargins(0, 0, 0, 0)
        lab_spinner_layout.setSpacing(5)
        
        lab_label = QLabel("Laboratory Units")
        lab_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 14px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        self.lab_spinner = QSpinBox()
        self.lab_spinner.setObjectName("LAB_SPINNER")
        self.lab_spinner.setRange(0, 5)
        self.lab_spinner.setValue(1)  # Default value
        self.lab_spinner.setFixedSize(113, 40)
        self.lab_spinner.setStyleSheet(f"""
            QSpinBox {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 16px;
            }}
            QSpinBox::up-button, QSpinBox::down-button {{
                width: 20px;
                border-left: 1px solid {self.ui_config['colors']['MID_TEAL']};
            }}
        """)
        
        lab_shadow = QGraphicsDropShadowEffect()
        lab_shadow.setBlurRadius(5)
        lab_shadow.setOffset(0, 2)
        lab_shadow.setColor(QColor(0, 0, 0, 30))
        self.lab_spinner.setGraphicsEffect(lab_shadow)
        
        lab_spinner_layout.addWidget(lab_label)
        lab_spinner_layout.addWidget(self.lab_spinner)
        lab_spinner_widget.setVisible(False)  # Initially hidden
        self.lab_spinner_widget = lab_spinner_widget  # Store reference for toggling visibility
        spinners_layout.addWidget(lab_spinner_widget)
        
        left_layout.addWidget(spinners_row)
        third_row_layout.addWidget(left_side)
        
        # Connect the radio button toggle to update lab spinner visibility
        self.has_lab_radio.toggled.connect(self.toggle_lab_spinner)
        
        # Template selection
        template_section = QWidget()
        template_layout = QVBoxLayout(template_section)
        template_layout.setContentsMargins(0, 0, 0, 0)
        template_layout.setSpacing(5)
        
        template_label = QLabel("Course Template")
        template_label.setStyleSheet(f"font-family: {self.ui_config['fonts']['BODY_FONT']}; font-size: 16px; color: {self.ui_config['colors']['DARK_TEAL']};")
        
        template_input_row = QWidget()
        template_input_layout = QHBoxLayout(template_input_row)
        template_input_layout.setContentsMargins(0, 0, 0, 0)
        template_input_layout.setSpacing(10)
        
        self.template_input = QLineEdit()
        self.template_input.setObjectName("TEMPLATE_BOX")
        self.template_input.setFixedHeight(40)
        self.template_input.setReadOnly(True)
        self.template_input.setPlaceholderText("Select Template")
        self.template_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                padding: 5px 10px;
                font-family: {self.ui_config['fonts']['BODY_FONT']};
                font-size: 14px;
                background-color: #F9F9F9;
            }}
        """)
        
        template_shadow = QGraphicsDropShadowEffect()
        template_shadow.setBlurRadius(5)
        template_shadow.setOffset(0, 2)
        template_shadow.setColor(QColor(0, 0, 0, 30))
        self.template_input.setGraphicsEffect(template_shadow)
        
        browse_button = QPushButton()
        browse_button.setFixedSize(40, 40)
        browse_button.setIcon(QIcon("./assets/folder_icon.png"))  # You'll need to have this icon
        browse_button.setIconSize(QSize(20, 20))
        browse_button.setStyleSheet(f"""
            QPushButton {{
                border: 1px solid {self.ui_config['colors']['MID_TEAL']};
                border-radius: 5px;
                background-color: {self.ui_config['colors']['MID_TEAL']};
            }}
            QPushButton:hover {{
                background-color: {self.ui_config['colors']['DARK_TEAL']};
            }}
        """)
        browse_button.clicked.connect(self.browse_template)
        
        template_input_layout.addWidget(self.template_input)
        template_input_layout.addWidget(browse_button)
        
        template_layout.addWidget(template_label)
        template_layout.addWidget(template_input_row)
        template_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        third_row_layout.addWidget(template_section)
        
        content_layout.addWidget(third_row)
        
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
        
        # Adding click event to close when clicking outside
        self.setStyleSheet("background-color: rgba(0, 0, 0, 80);")  # Semi-transparent background
        
    def toggle_lab_spinner(self, checked):
        """Toggle the visibility of the lab spinner based on radio button state"""
        self.lab_spinner_widget.setVisible(checked)
        
    def browse_template(self):
        """Open file dialog to select a template file"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Template", "", "JavaScript Files (*.js)", options=options
        )
        if file_name:
            # Display only the filename, not the full path
            self.template_input.setText(os.path.basename(file_name))
            
    def import_course(self):
        """Handle import course button click"""
        print("Clicked Import Course")
        
    def create_course(self):
        """Handle create course button click and database insertion"""
        print("Clicked Create Course")
        
        # Get values from input fields
        course_title = self.title_input.text()
        course_nickname = self.nickname_input.text()
        course_code = self.code_input.text()
        section = self.section_input.text()
        has_lab = self.has_lab_radio.isChecked()
        lec_units = self.lec_spinner.value()
        lab_units = self.lab_spinner.value() if has_lab else 0
        
        # Basic validation
        if not all([course_title, course_nickname, course_code, section]):
            print("All fields must be filled!")
            return
            
        try:
            # Connect to database
            conn = sqlite3.connect('db/gradebook.db')
            cursor = conn.cursor()
            
            # Insert lecture course
            cursor.execute("""
                INSERT INTO course (course_title, course_nickname, course_code, units, section, linked_courseID)
                VALUES (?, ?, ?, ?, ?, NULL)
            """, (course_title, course_nickname, course_code, lec_units, section))
            
            lec_course_id = cursor.lastrowid
            
            # If has lab, insert lab course
            if has_lab and lab_units > 0:
                lab_code = f"{course_code}L"
                lab_nickname = f"{course_nickname}-L"
                
                cursor.execute("""
                    INSERT INTO course (course_title, course_nickname, course_code, units, section, linked_courseID)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (course_title.replace("(LEC)", "(LAB)"), lab_nickname, lab_code, lab_units, section, lec_course_id))
            
            conn.commit()
            conn.close()
            
            print(f"Course created successfully! ID: {lec_course_id}")
            self.accept()  # Close dialog on success
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            
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

# For testing purposes
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    
    # Sample UI config
    ui_config = {
        'colors': {
            'MID_TEAL': '#2C8C99',
            'DARK_TEAL': '#0A2E36',
            'SNOW_WHITE': '#FFFFFF',
            'GRAY': '#888888'
        },
        'fonts': {
            'HEADING_FONT': 'Narnoor Medium',  # Replace with available font if needed
            'BODY_FONT': 'Inter'  # Replace with available font if needed
        },
        'dimensions': {
            'TITLE_SECTION_HEIGHT': 50
        }
    }
    
    dialog = AddNewCoursePopup(ui_config)
    dialog.show()
    
    sys.exit(app.exec_())