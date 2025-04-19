from PyQt5.QtGui import QFontDatabase

def load_fonts():
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Bold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-ExtraBold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Medium.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Regular.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-SemiBold.ttf")