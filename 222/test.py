# -*- coding: utf-8 -*-
import sys
from scene import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(500, 500)
        self.scene = Scene('test', self)
        self.role = Role(6, '11', 'pic.png', 35, 30)
        self.scene.addDynamic(self.role)
        self.role.addDownPoint(Point(0, 0))
        self.role.addDownPoint(Point(30, 0))
        self.role.addDownPoint(Point(60, 0))

        self.role.addUpPoint(Point(0, 96))
        self.role.addUpPoint(Point(32, 96))
        self.role.addUpPoint(Point(62, 96))

        self.role.addLeftPoint(Point(0, 32))
        self.role.addLeftPoint(Point(32, 32))
        self.role.addLeftPoint(Point(64, 32))

        self.role.addRightPoint(Point(0, 64))
        self.role.addRightPoint(Point(30, 64))
        self.role.addRightPoint(Point(61, 64))
        # self.scene.setBackground('3.jpg')
        # self.scene.setEnableScale(True)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.scene.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        self.role.goDown()
        # self.scene.move(self.scene.x - 1, self.scene.y - 1)
        # self.update()

    def keyPressEvent(self, event):
        pass

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.role.goLeft()
        elif event.key() == Qt.Key_Right:
            self.role.goRight()
        elif event.key() == Qt.Key_Up:
            self.role.goUp()
        elif event.key() == Qt.Key_Down:
            self.role.goDown()


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    timer = QTimer()
    timer.setInterval(11)
    timer.start()
    QObject.connect(timer, SIGNAL("timeout()"), win, SLOT("update()"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
