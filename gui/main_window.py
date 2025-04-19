from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from header_widget import HeaderWidget
from body_widget import BodyWidget
from footer_widget import FooterWidget

class MainWindow(QMainWindow):
    def __init__(self, ui_config=None):
        super().__init__()
        self.ui_config = ui_config 
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
        self.header = HeaderWidget(ui_config=self.ui_config)
        self.main_layout.addWidget(self.header)

        self.body = BodyWidget(ui_config=self.ui_config)
        self.main_layout.addWidget(self.body)

        self.footer = FooterWidget(ui_config=self.ui_config)
        self.main_layout.addWidget(self.footer)
