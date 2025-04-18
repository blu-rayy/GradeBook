import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QFrame)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Define colors and fonts
        self.mid_teal = "#145A5A"
        self.dark_teal = "#002832"
        self.green_teal = "#00674F"
        self.snow_white = "#E3F9FA"
        self.heading_font = QFont("Arial", 12)  # Placeholder for narnoor font
        self.body_font = QFont("Arial", 10)     # Placeholder for inter font
        
        self.setWindowTitle("Application Layout")
        self.resize(1920, 1080)
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Initialize UI components
        self.init_header()
        self.init_body()
        self.init_footer()
        
    def init_header(self):
        # HEADER - 1920x85
        self.header_widget = QWidget()
        self.header_widget.setFixedHeight(85)
        self.header_widget.setStyleSheet(f"background-color: {self.mid_teal};")
        
        header_layout = QHBoxLayout(self.header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)
        
        # LEFT_SECTION - 530x85
        self.header_left = QWidget()
        self.header_left.setFixedWidth(530)
        self.header_left.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        left_layout = QVBoxLayout(self.header_left)
        left_layout.addWidget(QLabel("LEFT_SECTION"))

        # Add separator line
        left_line = QFrame()
        left_line.setFrameShape(QFrame.VLine)
        left_line.setFrameShadow(QFrame.Sunken)
        left_line.setStyleSheet("color: white;")  # This line can be removed when development is complete
        
        # MIDDLE_SECTION - 860x85
        self.header_middle = QWidget()
        self.header_middle.setFixedWidth(860)
        self.header_middle.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
        middle_layout = QVBoxLayout(self.header_middle)
        middle_layout.addWidget(QLabel("MIDDLE_SECTION"))
        
        # Add separator line
        middle_line = QFrame()
        middle_line.setFrameShape(QFrame.VLine)
        middle_line.setFrameShadow(QFrame.Sunken)
        middle_line.setStyleSheet("color: white;")  # This line can be removed when development is complete
        
        # RIGHT_SECTION - 530x85
        self.header_right = QWidget()
        self.header_right.setFixedWidth(530)
        self.header_right.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        right_layout = QVBoxLayout(self.header_right)
        right_layout.addWidget(QLabel("RIGHT_SECTION"))
        
        # Add components to header
        header_layout.addWidget(self.header_left)
        header_layout.addWidget(left_line)  # Remove this line when development is complete
        header_layout.addWidget(self.header_middle)
        header_layout.addWidget(middle_line)  # Remove this line when development is complete
        header_layout.addWidget(self.header_right)
        
        # Add header to main layout
        self.main_layout.addWidget(self.header_widget)
        
        # Add separator line between HEADER and BODY
        header_separator = QFrame()
        header_separator.setFrameShape(QFrame.HLine)
        header_separator.setFrameShadow(QFrame.Sunken)
        header_separator.setStyleSheet("color: red;")  # This line can be removed when development is complete
        self.main_layout.addWidget(header_separator)
        
    def init_body(self):
        # BODY - 1780x913
        self.body_widget = QWidget()
        self.body_widget.setFixedSize(1780, 913)
        self.body_widget.setStyleSheet(f"background-color: {self.snow_white};")
        
        # Center the body widget
        body_container = QWidget()
        body_container_layout = QHBoxLayout(body_container)
        body_container_layout.setAlignment(Qt.AlignCenter)
        body_container_layout.addWidget(self.body_widget)
        
        body_layout = QVBoxLayout(self.body_widget)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)
        
        # TITLE_SECTION - 1780x77
        self.title_section = QWidget()
        self.title_section.setFixedSize(1780, 77)
        self.title_section.setStyleSheet(f"background-color: {self.green_teal};")
        title_layout = QVBoxLayout(self.title_section)
        title_layout.addWidget(QLabel("TITLE_SECTION"))
        body_layout.addWidget(self.title_section)
        
        # Add separator line
        title_separator = QFrame()
        title_separator.setFrameShape(QFrame.HLine)
        title_separator.setFrameShadow(QFrame.Sunken)
        title_separator.setStyleSheet("color: blue;")  # This line can be removed when development is complete
        body_layout.addWidget(title_separator)
        
        # Create horizontal layout for the three sections
        sections_layout = QHBoxLayout()
        sections_layout.setContentsMargins(0, 0, 0, 0)
        sections_layout.setSpacing(0)
        
        # CS_OTHERS_SECTION - 682x836
        self.cs_others_section = QWidget()
        self.cs_others_section.setFixedSize(682, 836)
        self.cs_others_section.setStyleSheet("background-color: rgba(20, 90, 90, 0.1);")
        cs_others_layout = QVBoxLayout(self.cs_others_section)
        cs_others_layout.addWidget(QLabel("CS_OTHERS_SECTION"))
        sections_layout.addWidget(self.cs_others_section)
        
        # Add separator line
        others_separator = QFrame()
        others_separator.setFrameShape(QFrame.VLine)
        others_separator.setFrameShadow(QFrame.Sunken)
        others_separator.setStyleSheet("color: green;")  # This line can be removed when development is complete
        sections_layout.addWidget(others_separator)
        
        # CS_SA_EXAMS_SECTION - 584x836
        self.cs_sa_exams_section = QWidget()
        self.cs_sa_exams_section.setFixedSize(584, 836)
        self.cs_sa_exams_section.setStyleSheet("background-color: rgba(20, 90, 90, 0.2);")
        cs_sa_exams_layout = QVBoxLayout(self.cs_sa_exams_section)
        cs_sa_exams_layout.addWidget(QLabel("CS_SA_EXAMS_SECTION"))
        sections_layout.addWidget(self.cs_sa_exams_section)
        
        # Add separator line
        exams_separator = QFrame()
        exams_separator.setFrameShape(QFrame.VLine)
        exams_separator.setFrameShadow(QFrame.Sunken)
        exams_separator.setStyleSheet("color: green;")  # This line can be removed when development is complete
        sections_layout.addWidget(exams_separator)
        
        # GRADES_BREAKDOWN_SECTION - 514x836
        self.grades_breakdown_section = QWidget()
        self.grades_breakdown_section.setFixedSize(514, 836)
        self.grades_breakdown_section.setStyleSheet("background-color: rgba(20, 90, 90, 0.1);")
        grades_breakdown_layout = QVBoxLayout(self.grades_breakdown_section)
        grades_breakdown_layout.addWidget(QLabel("GRADES_BREAKDOWN_SECTION"))
        sections_layout.addWidget(self.grades_breakdown_section)
        
        body_layout.addLayout(sections_layout)
        self.main_layout.addWidget(body_container)
        
        # Add separator line between BODY and FOOTER
        body_separator = QFrame()
        body_separator.setFrameShape(QFrame.HLine)
        body_separator.setFrameShadow(QFrame.Sunken)
        body_separator.setStyleSheet("color: red;")  # This line can be removed when development is complete
        self.main_layout.addWidget(body_separator)
        
    def init_footer(self):
        # FOOTER - 1920x85
        self.footer_widget = QWidget()
        self.footer_widget.setFixedHeight(85)
        self.footer_widget.setStyleSheet(f"background-color: {self.dark_teal};")
        
        footer_layout = QHBoxLayout(self.footer_widget)
        footer_layout.setContentsMargins(0, 0, 0, 0)
        footer_layout.setSpacing(0)
        
        # HOME_SECTION - 80x80
        self.home_section = QWidget()
        self.home_section.setFixedWidth(80)
        self.home_section.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        home_layout = QVBoxLayout(self.home_section)
        home_layout.addWidget(QLabel("HOME"))
        footer_layout.addWidget(self.home_section)
        
        # Add separator line
        home_line = QFrame()
        home_line.setFrameShape(QFrame.VLine)
        home_line.setFrameShadow(QFrame.Sunken)
        home_line.setStyleSheet("color: white;")  # This line can be removed when development is complete
        footer_layout.addWidget(home_line)
        
        # COURSE_SECTION - 1760x80
        self.course_section = QWidget()
        self.course_section.setFixedWidth(1760)
        self.course_section.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
        course_layout = QVBoxLayout(self.course_section)
        course_layout.addWidget(QLabel("COURSE_SECTION"))
        footer_layout.addWidget(self.course_section)
        
        # Add separator line
        course_line = QFrame()
        course_line.setFrameShape(QFrame.VLine)
        course_line.setFrameShadow(QFrame.Sunken)
        course_line.setStyleSheet("color: white;")  # This line can be removed when development is complete
        footer_layout.addWidget(course_line)
        
        # NEXT_SECTION - 80x80
        self.next_section = QWidget()
        self.next_section.setFixedWidth(80)
        self.next_section.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        next_layout = QVBoxLayout(self.next_section)
        next_layout.addWidget(QLabel("NEXT"))
        footer_layout.addWidget(self.next_section)
        
        # Add footer to main layout
        self.main_layout.addWidget(self.footer_widget)
        
    def resizeEvent(self, event):
        """Handle resize events to maintain proportions and layout"""
        super().resizeEvent(event)
        # Add any dynamic resizing logic here if needed
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())