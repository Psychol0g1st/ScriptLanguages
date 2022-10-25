import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5 import QtGui

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "PDF Manipulator"
        self.top = 100
        self.left = 100
        self.width = 1024
        self.height = 1024
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))
        self.initWindow()


    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


def main():

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()