from image_1 import image
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
from PyQt5.QtCore import Qt


class FirstWid(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        self.delta = '0.005'
        im = image(self.delta)
        print(type(im))
        pixmap = QPixmap()
        pixmap.loadFromData(im)
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if float(self.delta) - 0.00001 > 0:
                self.delta = str(float(self.delta) + 0.0009)
                im = image(self.delta)
                pixmap = QPixmap()
                pixmap.loadFromData(im)
                self.label.setPixmap(pixmap)

        if event.key() == Qt.Key_PageDown:
            self.delta = str(float(self.delta) - 0.0009)
            im = image(self.delta)
            pixmap = QPixmap()
            pixmap.loadFromData(im)
            self.label.setPixmap(pixmap)
        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstWid()
    ex.show()
    sys.exit(app.exec_())
