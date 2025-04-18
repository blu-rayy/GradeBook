import sys
import os
from PyQt5.QtWidgets import QApplication
from constants import *
from load_font import load_fonts
from main_window import MainWindow

os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    load_fonts()

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
