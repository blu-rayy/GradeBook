import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# remove from to after debugging

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGraphicsDropShadowEffect, QSizePolicy, QFileDialog,QRadioButton, QSpinBox, QFileDialog
from PyQt5.QtGui import QColor, QPainterPath, QRegion, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QSize
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
        content_layout.setSpacing(10)
        
        # First row - Course Title
        title_row = QWidget()
        title_row_layout = QVBoxLayout(title_row)
        title_row_layout.setContentsMargins(0, 0, 0, 0)
        title_row_layout.setSpacing(0)

        input_group = QWidget()
        input_group.setFixedWidth(1009)
        input_group_layout = QHBoxLayout(input_group)
        input_group_layout.setContentsMargins(0, 0, 0, 0)
        input_group_layout.setSpacing(0)

        prefix_label = QLabel("Course Title")
        prefix_label.setObjectName("input_prefix")
        prefix_label.setFixedHeight(40)
        prefix_label.setFixedWidth(110)
        prefix_label.setAlignment(Qt.AlignCenter)

        self.title_input = QLineEdit()
        self.title_input.setFixedHeight(40)
        self.title_input.setObjectName("input")
        self.title_input.setPlaceholderText("e.g., Introduction to Computing (LEC)")

        input_group_layout.addWidget(prefix_label)
        input_group_layout.addWidget(self.title_input)
        title_row_layout.addWidget(input_group)
        content_layout.addWidget(title_row)

        # Second row - Course Nickname
        nickname_row = QWidget()
        nickname_row_layout = QHBoxLayout(nickname_row)
        nickname_row_layout.setContentsMargins(0, 0, 0, 0)
        nickname_row_layout.setSpacing(14)  # or 20 for more gap

        # Course Nickname
        nickname_input_group = QWidget()
        nickname_input_layout = QHBoxLayout(nickname_input_group)
        nickname_input_layout.setContentsMargins(0, 0, 0, 0)
        nickname_input_layout.setSpacing(0)

        nickname_prefix_label = QLabel("Course Nickname")
        nickname_prefix_label.setObjectName("input_prefix")
        nickname_prefix_label.setFixedHeight(40)
        nickname_prefix_label.setFixedWidth(150)
        nickname_prefix_label.setAlignment(Qt.AlignCenter)

        self.nickname_input = QLineEdit()
        self.nickname_input.setFixedHeight(40)
        self.nickname_input.setObjectName("input")
        self.nickname_input.setPlaceholderText("fifteen characters only (e.g., ITC CCS1)")

        nickname_input_layout.addWidget(nickname_prefix_label)
        nickname_input_layout.addWidget(self.nickname_input)

        # Course Code
        code_input_group = QWidget()
        code_input_group.setFixedWidth(330)
        code_input_layout = QHBoxLayout(code_input_group)
        code_input_layout.setContentsMargins(0, 0, 0, 0)
        code_input_layout.setSpacing(0)

        code_prefix_label = QLabel("Course Code")
        code_prefix_label.setObjectName("input_prefix")
        code_prefix_label.setFixedHeight(40)
        code_prefix_label.setFixedWidth(120)
        code_prefix_label.setAlignment(Qt.AlignCenter)

        self.code_input = QLineEdit()
        self.code_input.setFixedHeight(40)
        self.code_input.setObjectName("input")
        self.code_input.setPlaceholderText("e.g., CCS1")
        self.code_input.setFixedWidth(330 - 120)

        code_input_layout.addWidget(code_prefix_label)
        code_input_layout.addWidget(self.code_input)

        # Second row - Section
        section_input_group = QWidget()
        section_input_group.setFixedWidth(190)
        section_input_layout = QHBoxLayout(section_input_group)
        section_input_layout.setContentsMargins(0, 0, 0, 0)
        section_input_layout.setSpacing(0)

        section_prefix_label = QLabel("Section")
        section_prefix_label.setObjectName("input_prefix")
        section_prefix_label.setFixedHeight(40)
        section_prefix_label.setFixedWidth(70)
        section_prefix_label.setAlignment(Qt.AlignCenter)

        self.section_input = QLineEdit()
        self.section_input.setFixedHeight(40)
        self.section_input.setObjectName("input")
        self.section_input.setPlaceholderText("e.g., TN01")
        self.section_input.setFixedWidth(190 - 70)
        self.section_input.setMaximumWidth(120)

        section_input_layout.addWidget(section_prefix_label)
        section_input_layout.addWidget(self.section_input)

        nickname_row_layout.addWidget(nickname_input_group, 3)
        nickname_row_layout.addWidget(code_input_group, 2)     
        nickname_row_layout.addWidget(section_input_group, 2)  
        content_layout.addWidget(nickname_row)

        # Third row - Radio button, spinners, template selection
        third_row = QWidget()
        third_row_layout = QHBoxLayout(third_row)
        third_row_layout.setContentsMargins(0, 0, 0, 0)
        third_row_layout.setSpacing(10)
        
        # Radio button and lecture spinner group
        spinner_group = QWidget()
        spinner_group_layout = QHBoxLayout(spinner_group)
        spinner_group_layout.setContentsMargins(0, 0, 0, 0)
        spinner_group_layout.setSpacing(0)
        
        # Radio button
        self.has_lab_radio = QRadioButton()
        self.has_lab_radio.setObjectName("radio_button")
        self.has_lab_radio.setFixedSize(32, 32)
        self.has_lab_radio.setCursor(Qt.PointingHandCursor)
        
        lab_label = QLabel("Has Laboratory")
        
        # Lecture units label and spinner
        lec_label = QLabel("LEC")
        lec_label.setObjectName("input_prefix")
        lec_label.setFixedHeight(40)
        lec_label.setFixedWidth(60)
        lec_label.setAlignment(Qt.AlignCenter)
        
        self.lec_spinner = QSpinBox()
        self.lec_spinner.setObjectName("spinners")
        self.lec_spinner.setRange(0, 5)
        self.lec_spinner.setValue(2)
        self.lec_spinner.setFixedHeight(40)
        self.lec_spinner.setFixedWidth(80)
        
        # Layout for radio button group
        radio_group = QWidget()
        radio_layout = QHBoxLayout(radio_group)
        radio_layout.setContentsMargins(0, 0, 0, 0)
        radio_layout.setSpacing(6)
        radio_layout.addWidget(self.has_lab_radio)
        radio_layout.addWidget(lab_label)
        radio_layout.addStretch()
        
        # Lab units spinner
        lab_label = QLabel("LAB")
        lab_label.setObjectName("input_prefix")
        lab_label.setFixedHeight(40)
        lab_label.setFixedWidth(60)
        lab_label.setAlignment(Qt.AlignCenter)
        
        self.lab_spinner = QSpinBox()
        self.lab_spinner.setObjectName("spinners")
        self.lab_spinner.setRange(0, 5)
        self.lab_spinner.setValue(1)
        self.lab_spinner.setFixedHeight(40)
        self.lab_spinner.setFixedWidth(80)
        
        # Container for lab spinner
        lab_group = QWidget()
        lab_layout = QHBoxLayout(lab_group)
        lab_layout.setContentsMargins(0, 0, 0, 0)
        lab_layout.setSpacing(0)
        lab_layout.addWidget(lab_label)
        lab_layout.addWidget(self.lab_spinner)
        
        self.lab_group = lab_group 
        lab_group.setVisible(False)
        
        # Add lecture spinner
        lec_group = QWidget()
        lec_layout = QHBoxLayout(lec_group)
        lec_layout.setContentsMargins(0, 0, 0, 0)
        lec_layout.setSpacing(0)
        lec_layout.addWidget(lec_label)
        lec_layout.addWidget(self.lec_spinner)
        
        # Create the left side layout
        left_side = QWidget()
        left_layout = QHBoxLayout(left_side)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        left_layout.addWidget(radio_group)
        left_layout.addWidget(lec_group)
        left_layout.addWidget(lab_group)

        # Template selection
        template_group = QWidget()
        template_layout = QHBoxLayout(template_group)
        template_layout.setContentsMargins(0, 0, 0, 0)
        template_layout.setSpacing(0)
        
        template_prefix_label = QLabel("Select Template")
        template_prefix_label.setObjectName("input_prefix")
        template_prefix_label.setFixedHeight(40)
        template_prefix_label.setFixedWidth(140)
        template_prefix_label.setAlignment(Qt.AlignCenter)
        
        self.template_input = QLineEdit()
        self.template_input.setObjectName("input_template")
        self.template_input.setFixedHeight(40)
        self.template_input.setReadOnly(True)
        self.template_input.setPlaceholderText("only supports .json file extensions")
        
        browse_button = QPushButton()
        browse_button.setFixedSize(40, 40)
        browse_button.setIcon(QIcon(r"assets\icons\folder.png"))
        browse_button.setIconSize(QSize(24, 24))
        browse_button.setObjectName("browse_button")
        browse_button.setCursor(Qt.PointingHandCursor)

        browse_button.clicked.connect(self.browse_template)
        
        template_box_layout = QHBoxLayout()
        template_box_layout.setContentsMargins(0, 0, 0, 0)
        template_box_layout.setSpacing(0)
        template_box_layout.addWidget(self.template_input)
        template_box_layout.addWidget(browse_button)
        
        template_layout.addWidget(template_prefix_label)
        template_layout.addLayout(template_box_layout)
        
        # add to third row
        third_row_layout.addWidget(left_side, 1)
        third_row_layout.addWidget(template_group, 2)
        
        content_layout.addWidget(third_row)
        
        # Connect the radio button toggle to update lab spinner visibility
        self.has_lab_radio.toggled.connect(self.toggle_lab_spinner)
        
        # Button row
        button_row = QWidget()
        button_layout = QHBoxLayout(button_row)
        button_layout.setContentsMargins(0, 20, 0, 0)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(20)
        
        import_button = QPushButton("Import Course")
        import_button.setFixedSize(170, 40)
        import_button.setObjectName("bottom_button")


        import_button.clicked.connect(self.import_course)
        
        create_button = QPushButton("Create Course")
        create_button.setFixedSize(170, 40)
        create_button.setObjectName("bottom_button")
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
        
    def browse_template(self):
        """Open file dialog to select a template file"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Template", "", "JavaScript Files (*.json)", options=options
        )
        if file_name:
            # Display only the filename, not the full path
            self.template_input.setText(os.path.basename(file_name))
            
    def toggle_lab_spinner(self, checked):
        """Show or hide lab spinner based on radio button state"""
        # Use the direct reference to lab_group
        if hasattr(self, 'lab_group'):
            self.lab_group.setVisible(checked)
            
            # When lab is hidden, expand the template section
            if not checked:
                # Find the third_row QWidget
                third_row = None
                for i in range(self.findChild(QWidget, "content_section").layout().count()):
                    item = self.findChild(QWidget, "content_section").layout().itemAt(i).widget()
                    if item and item.layout() and item.layout().count() == 2:  # Third row has 2 items
                        left_side = item.layout().itemAt(0).widget()
                        template_group = item.layout().itemAt(1).widget()
                        if left_side and template_group:
                            # Update the stretch factors
                            item.layout().setStretch(0, 1)  # Compress left side
                            item.layout().setStretch(1, 3)  # Expand template
                            break
            else:
                # When lab is shown, restore original proportions
                for i in range(self.findChild(QWidget, "content_section").layout().count()):
                    item = self.findChild(QWidget, "content_section").layout().itemAt(i).widget()
                    if item and item.layout() and item.layout().count() == 2:
                        # Restore original stretch factors
                        item.layout().setStretch(0, 1)
                        item.layout().setStretch(1, 2)
                        break
        
    def select_template(self):
        """Open file dialog to select template file"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Template File",
            "",
            "JSON Files (*.json)",
            options=options
        )
        
        if file_name:
            # Extract just the filename from the path
            import os
            base_filename = os.path.basename(file_name)
            self.template_box.setText(base_filename)
            # Store the full path internally
            self.template_file_path = file_name
        
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
            self.accept()
            
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