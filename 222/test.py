# -*- coding: utf-8 -*-
import sys
from scene import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(100, 100)
        self.scene = Scene(self)
        self.scene.setBackground('3.jpg')
        self.scene.setEnableScale(True)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.scene.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        self.scene.move(self.scene.x - 1, self.scene.y - 1)
        self.update()


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
