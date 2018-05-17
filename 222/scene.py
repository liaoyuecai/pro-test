# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Role(object):
    def __init__(self, x=0, y=0, width=0, height=0):
        super(Role, self).__init__()
        self._x = x
        self._y = y
        self._sx = 0
        self._sy = 0
        self._width = width
        self._height = height
        self._scaleX = 1
        self._scaleY = 1
        self._rotation = 0
        self._opacity = 1
        self._selected = False

    def draw(self, p):
        pass

    # 设置透明度
    def setOpacity(self, opacity):
        self._opacity = opacity

    # 移动
    def move(self, x, y):
        self._x = x
        self._y = y

    # 顺时针旋转
    def clockwise(self, angle):
        self._rotation += angle
        if self._rotation > 360:
            self._rotation -= 360

    # 逆时针旋转
    def contrarotate(self, angle):
        self._rotation -= angle
        if self._rotation < 0:
            self._rotation += 360

    # 变形-缩放
    def scale(self, point):
        self._scaleX = (point.x() - self._x) / self._width
        self._scaleY = (point.y() - self._y) / self._height

    # 变形-横向拉伸
    def stretch_x(self, point):
        self._scaleX = (point.x() - self._x) / self._width

    # 变形-纵向拉伸
    def stretch_y(self, point):
        self._scaleY = (point.y() - self._y) / self._height

    # 鼠标点击
    def click(self, point, select):
        if select:
            if self._x <= point.x() <= (self._x + self._width) and self._y <= point.y() <= (self._y + self._height):
                # 选中
                self._selected = True
                return self
            else:
                # 取消选中
                self._selected = False
                return None
        else:
            self._selected = False
            return None

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @property
    def width(self):
        return self._width * self._scaleX

    @property
    def height(self):
        return self._height * self._scaleY


class Scene(Role):
    def __init__(self, parent):
        super(Scene, self).__init__(width=parent.width(), height=parent.height())
        self._background = None
        self._scale = False
        self._staticDict = {}
        self._dynamicDict = {}
        self._staticList = []
        self._dynamicList = []

    def setEnableScale(self, scale):
        self._scale = scale

    def setBackground(self, background):
        self._background = background

    def draw(self, p):
        if self._background:
            image = QImage()
            image.load(self._background)
            if not image.isNull():
                p.save()
                if self._scale:
                    self._scaleX = float(self._width) / float(image.width())
                    self._scaleY = float(self._height) / float(image.height())
                    if self._scaleX > self._scaleY:
                        self._scaleY = self._scaleX
                    else:
                        self._scaleX = self._scaleY
                    p.scale(self._scaleX, self._scaleY)
                p.drawImage(self._x, self._y, image, self._sx, self._sy)
                p.restore()
            for s in self._staticList:
                s.draw(p)
            for s in self._staticList:
                s.draw(p)


class Picture(Role):
    def __init__(self, url):
        super(Role, self).__init__()
        self.url = url

    def draw(self, p):
        image = QImage()
        image.load(self._url)
        if not image.isNull():
            p.save()
            if self._opacity is not 1:
                p.setOpacity(self._opacity * p.opacity())
            self._width = image.width()
            self._height = image.height()
            p.scale(self._scaleX, self._scaleY)
            if self._rotation is not 0:
                p.translate(self._width / 2, self._height / 2)
                p.rotate(self._rotation)
                p.translate(-self._width / 2, -self._height / 2)
            p.drawImage(self._x, self._y, image, self.sx, self.sy, self.width, self.height)
            p.restore()


class DynamicPic(Picture):
    def __init__(self, url):
        super(Role, self).__init__(url)
