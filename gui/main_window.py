from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from constants import *
from header_widget import HeaderWidget
from body_widget import BodyWidget
from footer_widget import FooterWidget
from ui_components import create_separator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GradeBook")
        self.resize(1920, 1080)
        self.setMinimumSize(1024, 768)

        # Central widget & layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add custom widgets
        self.header = HeaderWidget()
        self.main_layout.addWidget(self.header)

        self.body = BodyWidget()
        self.main_layout.addWidget(self.body)

        self.main_layout.addWidget(create_separator("horizontal", "red"))

        self.footer = FooterWidget()
        self.main_layout.addWidget(self.footer)
