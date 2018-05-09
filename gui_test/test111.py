# -*- coding: UTF8 -*-
from PyQt4 import QtGui, QtCore
import sys


class CanvasWidget(QtGui.QWidget):
    def __init__(self):
        super(CanvasWidget, self).__init__()

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
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
        image.load('2.bmp')
        # 旋转
        canvas.rotate(30)
        # （x，y）指定要绘制的绘画设备中的左上角点。（sx，sy）指定要绘制的图像中的左上角点。默认值是（0，0）。（sw，sh）指定要绘制的图像的大小。默认值（0，0）（和负值）表示一直到图像的右下角。
        canvas.drawImage(50, 50, image, 0, 0, 100, 100)
        # 结束绘画。释放绘画时使用的任何资源。因为它被析构函数调用，所以通常不需要调用它。
        canvas.end()

        wordpad = QtGui.QPainter()
        # 开始写字
        wordpad.begin(icon)
        pen = QtGui.QPen()
        colorObj = QtGui.QColor()
        colorObj.setNamedColor('#000000')
        pen.setColor(colorObj)

        #解决中文乱码问题
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


app = QtGui.QApplication(sys.argv)
icon = CanvasWidget()
icon.show()
sys.exit(app.exec_())
