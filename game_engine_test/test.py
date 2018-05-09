# -*- coding: UTF8 -*-
from PyQt4 import QtGui, QtCore
import sys

class Object(object):
    latestObjectIndex = 0

    def __init__(self):
        Object.latestObjectIndex += 1

        self.objectIndex = Object.latestObjectIndex


# 管理一些全局的事物吧，比如说获取窗口的大小，设置窗口刷新频率，向最低层加入显示对象等等
class Stage(Object):
    def __init__(self):
        super(Stage, self).__init__()
        self.parent = "root"
        self.width = 0
        self.height = 0
        self.speed = 0
        self.app = None
        self.canvasWidget = None
        self.canvas = None
        self.timer = None
        self.childList = []
        self.backgroundColor = None

    # 用来完成创建绘画设备和QPainter以及重绘计时器
    def _setCanvas(self, speed, title, width, height):
        self.speed = speed
        self.width = width
        self.height = height
        self.canvas = QtGui.QPainter()
        self.canvasWidget = CanvasWidget()
        self.canvasWidget.setWindowTitle(title)
        self.canvasWidget.setFixedSize(width, height)
        self.canvasWidget.show()
        ''' Qt的QTimer是一个计时器类，通过调用setInterval方法来设置计时时间，
                并循环计时。start方法开启计时器。然后还用到了connect方法来连接信号和槽，
                信号是“计时完毕”，槽是“刷新窗口”'''
        self.timer = QtCore.QTimer()
        self.timer.setInterval(speed)
        self.timer.start()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.canvasWidget, QtCore.SLOT("update()"))

    def _onShow(self):
        self.canvas.begin(self.canvasWidget)
        if self.backgroundColor is not None:
            self.canvas.fillRect(0, 0, self.width, self.height, getColor(self.backgroundColor))
        else:
            self.canvas.eraseRect(0, 0, self.width, self.height)
        self._showDisplayList(self.childList)
        self.canvas.end()

    def _showDisplayList(self, childList):
        for o in childList:
            if hasattr(o, "_show") and hasattr(o._show, "__call__"):
                o._show(self.canvas)

    def addChild(self, child):
        if child is not None:
            child.parent = self
            self.childList.append(child)
        else:
            raise ValueError("parameter 'child' must be a display object.")

    def removeChild(self, child):
        if child is not None:
            self.childList.remove(child)
            child.parent = None
        else:
            raise ValueError("parameter 'child' must be a display object.")


class CanvasWidget(QtGui.QWidget):
    def __init__(self):
        super(CanvasWidget, self).__init__()

    def paintEvent(self, event):
        stage._onShow()


def getColor(color):
    if isinstance(color, QtGui.QColor):
        return color
    elif not color:
        return QtCore.Qt.transparent
    else:
        colorObj = QtGui.QColor()
        colorObj.setNamedColor(color)
        return colorObj


def init(speed, title, width, height, callback):
    stage.app = QtGui.QApplication(sys.argv)
    stage._setCanvas(speed, title, width, height)

    if not hasattr(callback, "__call__"):
        raise ValueError("parameter 'callback' must be a function.")
    callback()
    stage.app.exec_()

def addChild(self, child):
    stage.addChild(child=child)

stage = Stage()

