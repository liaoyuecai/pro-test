# -*- coding: UTF8 -*-
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtCore import *
import sys

'''
调色板:   palette    铺平整个背景 （小于窗体有多个图片）
png 如果有图层，背景为黑色，可图层覆盖
'''


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(256, 256)
        self.setWindowTitle('Icon')
        mylayout = QVBoxLayout()
        self.setLayout(mylayout)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def paintEvent(self, event):
        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))  # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('1.bmp')))  # 设置背景图片
        self.setPalette(palette1)


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
