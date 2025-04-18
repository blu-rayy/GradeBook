import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase
from constants import *
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Bold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-ExtraBold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Medium.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Regular.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-SemiBold.ttf")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
