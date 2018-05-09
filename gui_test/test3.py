# -*- coding: UTF8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class ShapeWidget(QWidget):
    def __init__(self, parent=None):
        super(ShapeWidget, self).__init__(parent)
        self.i = 1
        self.mypix()
        self.timer = QTimer()
        self.timer.setInterval(500)  # 500秒
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    # 显示不规则 pic
    def mypix(self):
        self.update()
        if self.i == 5:
            self.i = 1
        self.mypic = {1: '1.bmp', 2: "2.bmp", 3: '3.bmp', 4: 'timg.jpg'}
        self.pix = QPixmap(self.mypic[self.i], "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)  #
        self.resize(self.pix.size())
        self.setMask(
            self.pix.mask())  # setMask()的作用是为调用它的控件增加一个遮罩，遮住所选区域以外的部分使之看起来是透明的， 它的参数可为一个QBitmap对象或一个QRegion对象，此处调用QPixmap的mask()函数获得图片自身的遮罩，为一个QBitmap对象。实例中使用的是png格式的图片，它的透明部分实际上即是一个遮罩。
        self.dragPosition = None

        # 重定义鼠标按下响应函数mousePressEvent(QMouseEvent)和鼠标移动响应函数mouseMoveEvent(QMouseEvent)，使不规则窗体能响应鼠标事件，随意拖动。

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()  # 保存当前鼠标点所在的位置相对于窗体左上角的偏移值dragPosition，
            event.accept()
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)  # 当左键移动窗体修改偏移值
            event.accept()
            # 如何激活 paintEvent 呢？ 一般 paintEvent 在窗体首次绘制加载， 要重新加载paintEvent 需要重新加载窗口使用 self.update() or  self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
        # 鼠标双击事件

    def mouseDoubleClickEvent(self, event):
        if event.button() == 1:
            self.i += 1
            self.mypix()

    # 每**秒修改paint

    def timeChange(self):
        self.i += 1
        self.mypix()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShapeWidget()
    form.show()
    app.exec_()
