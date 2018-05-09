# -*- coding: UTF8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

'''
 绘制QPainter 窗体    显示一个
 QPainter默认只能在paintEvent里面调用   否则：QPainter::begin: Paint device returned engine == 0, type: 1
'''


class MyForm(QWidget):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.resize(256, 256)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.drawPixmap(0, 0, 256, 256, QPixmap("timg.jpg"))
        painter.end()


app = QApplication([])
form = MyForm()
form.show()
app.exec_()
