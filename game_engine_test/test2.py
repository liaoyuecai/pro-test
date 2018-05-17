# -*- coding:utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Rotate")
        self.resize(500, 500)
        self.t = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        print(self.rect().x())
        print(self.rect().y())
        painter.drawText(self.rect(), Qt.AlignCenter, "text ......")

        painter.setPen(QColor(255, 0, 0))

        # painter.resetTransform()

        painter.translate(100, 100)

        painter.rotate(self.t)
        painter.drawRect(-25, -20, 50, 40)
        #
        # painter.resetTransform()
        #
        # painter.setPen(QColor(255, 0, 255))
        # painter.translate(200, 200)
        # painter.rotate(20)
        # painter.drawRect(-50, -40, 100, 80)
        #
        # painter.resetTransform()

        painter.end()

    def mousePressEvent(self, event):
        self.t += 10
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWnd = MainWindow()
    mainWnd.show()
    sys.exit(app.exec_())
