# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore


class DisplayObject(object):
    def __init__(self):
        super(DisplayObject, self).__init__()

        self.parent = None
        self.x = 0
        self.y = 0
        self.alpha = 1
        self.rotation = 0
        self.scaleX = 1
        self.scaleY = 1
        self.visible = True

    @property
    def width(self):
        return self._getOriginalWidth() * abs(self.scaleX)

    @property
    def height(self):
        return self._getOriginalHeight() * abs(self.scaleY)

    def _show(self, c):
        if not self.visible:
            return
        c.save()
        c.translate(self.x, self.y)
        c.setOpacity(self.alpha * c.opacity())
        c.rotate(self.rotation)
        c.scale(self.scaleX, self.scaleY)
        self._loopDraw(c)
        c.restore()

    def _loopDraw(self, c):
        pass

    def _getOriginalWidth(self):
        return 0

    def _getOriginalHeight(self):
        return 0

    def remove(self):
        self.parent.removeChild(self)


class Loader(DisplayObject):
    def __init__(self):
        super(Loader, self).__init__()

        self.content = None

    def load(self, url):
        image = QtGui.QImage()
        image.load(url)

        self.content = image


class BitmapData(object):
    def __init__(self, image=QtGui.QImage(), x=0, y=0, width=0, height=0):
        super(BitmapData, self).__init__()

        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if image is not None:
            if width == 0:
                self.width = image.width()

            if height == 0:
                self.height = image.height()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value > self.image.width():
            value = self.image.width()

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value > self.image.height():
            value = self.image.height()

        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (value + self.x) > self.image.width():
            value = self.image.width() - self.x

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (value + self.y) > self.image.height():
            value = self.image.height() - self.y

        self.__height = value

    def setCoordinate(self, x=0, y=0):
        self.x = x
        self.y = y

    def setProperties(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Bitmap(DisplayObject):
    def __init__(self, bitmapData=BitmapData()):
        super(Bitmap, self).__init__()
        self.bitmapData = bitmapData

    def _getOriginalWidth(self):
        return self.bitmapData.width

    def _getOriginalHeight(self):
        return self.bitmapData.height

    def _loopDraw(self, c):
        bmpd = self.bitmapData
        c.drawImage(0, 0, bmpd.image, bmpd.x, bmpd.y, bmpd.width, bmpd.height)

from test import init,addChild


def main():
    loader = Loader()
    loader.load("1.bmp")
    bmpd = BitmapData(loader.content)
    bmp = Bitmap(bmpd)
    addChild(bmp)

    bmp.x = 80
    bmp.y = 100
    bmp.rotation = -20
    bmp.alpha = 0.8

init(30, "Display An Image", 800, 600, main)