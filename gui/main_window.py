from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFrame
from constants import *
from header_widget import HeaderWidget
from body_widget import BodyWidget
from footer_widget import FooterWidget
from ui_components import create_separator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Layout")
        self.resize(1920, 1080)
        self.setMinimumSize(1024, 768)  # Set minimum size to prevent too small resizing
        
        # Set up central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Add the header widget
        self.header = HeaderWidget()
        self.main_layout.addWidget(self.header)
        
        # Add separator
        self.main_layout.addWidget(create_separator("horizontal", "red"))
        
        # Add the body widget
        self.body = BodyWidget()
        self.main_layout.addWidget(self.body)
        
        # Add separator
        self.main_layout.addWidget(create_separator("horizontal", "red"))
        
        # Add the footer widget
        self.footer = FooterWidget()
        self.main_layout.addWidget(self.footer)