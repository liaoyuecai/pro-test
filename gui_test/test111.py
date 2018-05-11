# -*- coding: UTF8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

list = [];


class Rectangle(object):
    startX = None
    startY = None
    endX = None
    endY = None

    def __init__(self):
        super(Rectangle, self).__init__()


class pic(object):
    x = 0;
    y = 0;
    img = None

    def __init__(self):
        super(self).__init__()

    def show(self, x, y, url):
        self.x = x
        self.y = y
        image = QtGui.QImage()
        image.load(url)
        self.img = image


class CanvasWidget(QtGui.QWidget):
    x = 0
    y = 0
    mouseStatus = False
    rectangle = None

    def __init__(self):
        super(CanvasWidget, self).__init__()
        self.setMouseTracking(True)
        # self.statusBar().showMessage('Ready')

    def paintEvent(self, event):
        # timer = QtCore.QTimer()
        # timer.setInterval(1000)
        # timer.start()
        # QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"), self, QtCore.SLOT("update()"))

        canvas = QtGui.QPainter()
        list.append(canvas)
        # 开始绘图
        canvas.begin(icon)
        # 擦除给定矩形内的区域
        # canvas.eraseRect(0, 0, 50, 50)
        # 保存当前状态（将状态推入堆栈）。save（）后面必须跟一个相应的restore（）
        # canvas.save()
        # 按给定的偏移量转换坐标系; 即给定的偏移量被添加到点
        # canvas.translate(1, 1)
        # 将不透明度设置为不透明度。值应该在0.0到1.0的范围内，其中0.0是完全透明的，1.0是完全不透明的
        # canvas.setOpacity(1 * canvas.opacity())
        # 恢复当前状态（从堆栈中弹出保存的状态）
        # canvas.rotate()
        # （sx，sy）缩放坐标系。
        # canvas.scale(1, 1)
        image = QtGui.QImage()
        f = open('2.bmp', "rb")
        data = f.read()
        f.close()
        image.loadFromData(data)
        # image.load('2.bmp')
        # 旋转
        canvas.rotate(30)
        # （x，y）指定要绘制的绘画设备中的左上角点。（sx，sy）指定要绘制的图像中的左上角点。默认值是（0，0）。（sw，sh）指定要绘制的图像的大小。默认值（0，0）（和负值）表示一直到图像的右下角。
        canvas.drawImage(self.x, self.y, image, 0, 0, 100, 100)
        # 结束绘画。释放绘画时使用的任何资源。因为它被析构函数调用，所以通常不需要调用它。
        # self.update()
        # canvas.end()

        wordpad = QtGui.QPainter()
        # 开始写字
        wordpad.begin(icon)
        pen = QtGui.QPen()
        colorObj = QtGui.QColor()
        colorObj.setNamedColor('#000000')
        pen.setColor(colorObj)
        if self.rectangle:
            # self.drawRect(wordpad)
            self.drawBorder(wordpad)

        # 解决中文乱码问题
        # QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf-8"))
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))
        # QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("utf-8"))
        font = QtGui.QFont()
        # 字体
        font.setFamily("Arial")
        font.setPixelSize(15)
        # font.setWeight(QtGui.QFont.Normal)
        # font.setWeight(QtGui.QFont.Bold)
        # font.setWeight(QtGui.QFont.Black)
        font.setWeight(QtGui.QFont.Light)
        font.setItalic(False)
        wordpad.setFont(font)
        wordpad.setPen(pen)
        # (x,y)左上角坐标,(x,y)宽 高
        wordpad.drawText(10, 10, 150, 50, QtCore.Qt.AlignCenter, 'aadds')
        # 结束写字
        wordpad.end()
        self.x += 1
        self.y += 1

    startX = None
    startY = None

    def mousePressEvent(self, event):
        self.mouseStatus = True
        self.rectangle = Rectangle()
        self.rectangle.startX = event.x()
        self.rectangle.startY = event.y()
        # image = QtGui.QImage()
        # image.load('3.bmp')
        # list[0].eraseRect(50, 50, 50, 50)
        # list[0].drawImage(50, 50, image, 0, 0, 50, 50)
        # button = event.button()
        # if button == 1:
        #     print('点击左键')
        #     # self.drawPoints(event.globalX(), event.globalY(), '#000000', 1)
        # elif button == 2:
        #     print('点击右键')

    def mouseMoveEvent(self, event):
        if self.mouseStatus:
            self.rectangle.endX = event.x()
            self.rectangle.endY = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.mouseStatus = False
        self.update()

    def wheelEvent(self, event):
        # -120向上 120向下
        button = event.delta()
        print(button)
        # if button == 1:
        #     print('点击左键')
        # elif button == 2:
        #     print('点击右键')

    def drawPoints(self, x, y, color, size):
        qp = QPainter()
        qp.begin(self)
        pen = QtGui.QPen()
        colorObj = QtGui.QColor()
        colorObj.setNamedColor(color)
        pen.setColor(colorObj)
        pen.setWidth(size)
        qp.setPen(pen)
        qp.drawPoint(x, y)
        qp.end()

    def drawLines(self, start_x, start_y, end_x, end_y, color, size):  #######画线
        qp = QPainter()
        qp.begin(self)
        pen = QtGui.QPen()
        colorObj = QtGui.QColor()
        colorObj.setNamedColor(color)
        pen.setColor(colorObj)
        pen.setWidth(size)
        qp.setPen(pen)
        qp.drawLine(start_x, start_y, end_x, end_y)
        qp.end()

    def drawBorder(self, qp):  #######画线
        intervalX = self.rectangle.endX - self.rectangle.startX
        intervalY = self.rectangle.endY - self.rectangle.startY
        interval_x = intervalX * 0.2
        interval_y = intervalY * 0.2
        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.drawRoundRect(self.rectangle.startX, self.rectangle.startY, self.rectangle.endX, self.rectangle.endY,50,50)
        # qp.drawLine(self.rectangle.startX + interval_x, self.rectangle.startY, self.rectangle.endX - interval_x,
        #             self.rectangle.startY)
        # qp.drawLine(self.rectangle.startX + interval_x, self.rectangle.endY, self.rectangle.endX - interval_x,
        #             self.rectangle.endY)
        # qp.drawLine(self.rectangle.startX, self.rectangle.startY + interval_y, self.rectangle.startX,
        #             self.rectangle.endY - interval_y)
        # qp.drawLine(self.rectangle.endX, self.rectangle.startY + interval_y, self.rectangle.endX,
        #             self.rectangle.endY - interval_y)
        # qp.drawArc(self.rectangle.startX - 2*interval_x, self.rectangle.startY - 2*interval_y, interval_x, interval_y, 1440,
        #            1440)

    def drawRect(self, qp):
        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.drawRect(self.rectangle.startX, self.rectangle.startY, self.rectangle.endX - self.rectangle.startX,
                    self.rectangle.endY - self.rectangle.startY)
    #
    # def drawEllipse(self, qp):  ########椭圆，圆
    #     qp.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
    #     qp.drawEllipse(100, 200, 300, 300)


def show_all():
    pass


app = QtGui.QApplication(sys.argv)
icon = CanvasWidget()
icon.show()
timer = QtCore.QTimer()
timer.setInterval(1000)
timer.start()
# QWidget.update() 通过立即调用paintEvent()来直接重新绘制窗口部件
# QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"), icon, QtCore.SLOT("update()"))
sys.exit(app.exec_())
