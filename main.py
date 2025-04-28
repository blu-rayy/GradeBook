import sys
import os
from PyQt5.QtWidgets import QApplication

from load_utils import *
from gui.main_window import MainWindow
from gui.config_loader import UI_CONFIG

os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## pip install -r requirements.txt

    load_fonts()
    load_tables(r'db/gradebook.db', r'db/schema.sql')

    window = MainWindow(ui_config=UI_CONFIG)
    window.show()
    sys.exit(app.exec_())