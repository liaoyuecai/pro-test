# -*- coding: UTF8 -*-
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))  # 设置背景颜色
        # palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('../../../Document/images/17_big.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)  # 不设置也可以
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        # self.setWindowIcon(QtGui.QIcon('../../../Document/images/firefox.png'))
        mylayout = QVBoxLayout()
        self.setLayout(mylayout)


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
