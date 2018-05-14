# -*- coding: utf-8 -*-

from PyQt4.QtGui import *


class Region(object):
    def __init__(self, width, height):
        super(Region, self).__init__()
        self._scaleX = 1
        self._scaleY = 1
        self._selected = False
        self._x = 0
        self._y = 0
        self._width = width
        self._height = height

    def __init__(self):
        super(Region, self).__init__()
        self._scaleX = 1
        self._scaleY = 1
        self._selected = False
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    # 移动
    def move(self, x, y):
        self._x = x
        self._y = y

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
    def click(self, point):
        if self._x <= point.x() <= (self._x + self.width) and self._y <= point.y() <= (self._y + self.height):
            return self
        else:
            return None

    # 选中
    def select(self):
        self._selected = True

    # 右键菜单
    def menu(self, point):
        pass

    def draw(self, p):
        pass

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

    @property
    def select(self):
        return self._selected


class Picture(Region):
    def __init__(self, img):
        super(Picture, self).__init__()
        self.image = QImage()
        self.image.load(img)
        size = self.image.size()
        self._width = size.width()
        self._height = size.height()
        self.sx = 0
        self.sy = 0

    def draw(self, p):
        p.save()
        # p.translate(self.x, self.y)
        # p.setOpacity(self.alpha * p.opacity())
        # p.rotate(self.rotation)
        p.scale(self._scaleX, self._scaleY)
        p.drawImage(self._x, self._y, self.image, self.sx, self.sy, self.width, self.height)
        p.restore()
