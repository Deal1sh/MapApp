from def_api import api
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys


class FirstWid(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        im = image()
        print(type(im))
        pixmap = QPixmap()
        pixmap.loadFromData(im)
        self.label.setPixmap(pixmap)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstWid()
    ex.show()
    sys.exit(app.exec_())
