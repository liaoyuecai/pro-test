# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Area(object):
    def __init__(self, name, x=0, y=0, width=0, height=0):
        self._name = name
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def isIn(self, point):
        if self._x <= point.x() <= (self._x + self._width) and self._y <= point.y() <= (self._y + self._height):
            return True
        else:
            return False

    @property
    def name(self):
        return self._name

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height


class Element(Area):
    def __init__(self, name, parent=None, x=0, y=0, width=0, height=0):
        super(Element, self).__init__(x, y, width, height)
        self._name = name
        self._sx = 0
        self._sy = 0
        self._scaleX = 1
        self._scaleY = 1
        self._rotation = 0
        self._opacity = 1
        self.parent = parent
        self._selected = False
        self._childDict = {}
        self._childList = []

    def addChild(self, s):
        s.bindScene(self)
        self._childList.append(s)
        self._childDict[s.name] = self._childList.index(s)

    def getChild(self, name):
        return self._childDict[name]

    @property
    def childList(self):
        return self._childList

    def isIn(self, point):
        if self._x <= point.x() <= (self._x + self.width) and self._y <= point.y() <= (self._y + self.height):
            return True
        else:
            return False

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
            if self.isIn(point):
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
    def width(self):
        return self._width * self._scaleX

    @property
    def height(self):
        return self._height * self._scaleY


class Scene(Element):
    def __init__(self, name, parent):
        super(Scene, self).__init__(name=name, width=parent.width(), height=parent.height())
        self._background = None
        self._scale = False

    def setEnableScale(self, scale):
        self._scale = scale

    def setBackground(self, background):
        self._background = background

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

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
        for s in self._dynamicList:
            s.draw(p)


class Map(Scene):
    def __init__(self, name, parent):
        super(Map, self).__init__(name, parent)
        self.disableAreas = []
        self.disableAreasDict = {}

    def addDisableArea(self, name, area):
        self.disableAreasDict[name] = area
        self.disableAreas.append(area)

    def removeDisableArea(self, name):
        area = self.disableAreasDict[name]
        if area:
            del self.disableAreasDict[name]
            self.disableAreas.remove(area)

    def isAbleIn(self, point):
        for area in self.disableAreas:
            if area.isIn(point):
                return area
        return None


class Item(Element):
    def __init__(self, parent, name):
        super(Picture, self).__init__(name, parent=parent)
        self.disable = False

    def setDisable(self, flag):
        self.disable = flag

    def getScene(self):
        if self.parent is None:
            return self
        else:
            return self.getScene()


class Picture(Item):
    def __init__(self, parent, name, url, width=0, height=0):
        super(Picture, self).__init__(parent, name)
        self._url = url
        self._width = width
        self._height = height

    def draw(self, p):
        if self.disable:
            return
        if self._url:
            image = QImage()
            image.load(self._url)
            if not image.isNull():
                p.save()
                if self._opacity is not 1:
                    p.setOpacity(self._opacity * p.opacity())
                if self._width == 0:
                    self._width = image.width()
                if self._height == 0:
                    self._height = image.height()
                p.scale(self._scaleX, self._scaleY)
                if self._rotation is not 0:
                    p.translate(self._width / 2, self._height / 2)
                    p.rotate(self._rotation)
                    p.translate(-self._width / 2, -self._height / 2)
                p.drawImage(self._x, self._y, image, self._sx, self._sy, self.width, self.height)
                p.restore()


class Door(Picture):
    enter = pyqtSignal(name='enter')

    def __init__(self, parent, name, exitPoint, goto, width, height, url=None):
        super(Door, self).__init__(name, parent, url, width, height)
        self._goto = goto
        self.exitPoint = exitPoint

    def isEnter(self, r):
        if self._x <= r.x and r.x + r.width <= (self._x + self.width) and self._y <= r.y and r.y + r.height <= (
                self._y + self.height):
            self.enter.emit()
            return True
        else:
            return False

    @property
    def goto(self):
        return self._goto

    def getExitPointX(self):
        return self.exitPoint.x

    def getExitPointY(self):
        return self.exitPoint.y


class Point(object):
    def __init__(self, x, y):
        super(Point, self).__init__()
        self._x = x
        self._y = y

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    def reset(self, x, y):
        self._x = x
        self._y = y


class DynamicPic(Picture):
    def __init__(self, parent, name, url, width, height):
        super(DynamicPic, self).__init__(parent, name, url, width=width, height=height)
        self.movingScrolls = []
        self.scrollPointer = 0
        self.speed = 10
        self.scrollTimer = None

    def addMovingPoint(self, point):
        self.movingScrolls.append(point)

    def clearScrolls(self):
        self.stop()
        self.movingScrolls = []

    def scroll(self):
        if self.scrollPointer > len(self.movingScrolls) - 1:
            self.scrollPointer = 0
        self._sx = self.movingScrolls[self.scrollPointer].x
        self._sy = self.movingScrolls[self.scrollPointer].y
        self.scrollPointer += 1

    def start(self, speed):
        if len(self.movingScrolls) > 0:
            self.scrollTimer = QTimer()
            self.scrollTimer.isActive()
            self.scrollTimer.setInterval(11)
            self.scrollTimer.start()
            self.speed = speed

    def stop(self):
        if self.scrollTimer and self.scrollTimer.isActive():
            self.scrollTimer.stop()


class Role(DynamicPic):

    def __init__(self, parent, stepSize, name, url, width, height):
        super(Role, self).__init__(parent, name, url, width, height)
        self.stepSize = stepSize
        self.upPoints = []
        self.downPoints = []
        self.leftPoints = []
        self.rightPoints = []
        self.upPointer = 0
        self.downPointer = 0
        self.leftPointer = 0
        self.rightPointer = 0

    def addUpPoint(self, point):
        self.upPoints.append(point)

    def addDownPoint(self, point):
        self.downPoints.append(point)

    def addLeftPoint(self, point):
        self.leftPoints.append(point)

    def addRightPoint(self, point):
        self.rightPoints.append(point)

    def resetStepSize(self, stepSize):
        self.stepSize = stepSize

    def goUp(self):
        if len(self.upPoints) > 0:
            if self.upPointer > len(self.upPoints) - 1:
                self.upPointer = 0
            self._sx = self.upPoints[self.upPointer].x
            self._sy = self.upPoints[self.upPointer].y
            self.upPointer += 1
        if self._y >= self.stepSize:
            if self.getScene().isIn(Point(self._x, self._y - self.stepSize)):
                self._y -= self.stepSize
                self.checkEvent()

    def goDown(self):
        if len(self.downPoints) > 0:
            if self.downPointer > len(self.downPoints) - 1:
                self.downPointer = 0
            self._sx = self.downPoints[self.downPointer].x
            self._sy = self.downPoints[self.downPointer].y
            self.downPointer += 1
        if self._y + self.stepSize < self.scene.width:
            if self.scene:
                if self.getScene().isIn(Point(self._x, self._y + self.stepSize)):
                    self._y += self.stepSize
                    self.checkEvent()

    def goLeft(self):
        if len(self.leftPoints) > 0:
            if self.leftPointer > len(self.leftPoints) - 1:
                self.leftPointer = 0
            self._sx = self.leftPoints[self.leftPointer].x
            self._sy = self.leftPoints[self.leftPointer].y
            self.leftPointer += 1
        if self._x >= self.stepSize:
            if self.getScene().isIn(Point(self._x - self.stepSize, self._y)):
                self._x -= self.stepSize
                self.checkEvent()

    def goRight(self):
        if len(self.rightPoints) > 0:
            if self.rightPointer > len(self.rightPoints) - 1:
                self.rightPointer = 0
            self._sx = self.rightPoints[self.rightPointer].x
            self._sy = self.rightPoints[self.rightPointer].y
            self.rightPointer += 1
        if self._x + self.stepSize < self.scene.height:
            if self.getScene().isIn(Point(self._x + self.stepSize, self._y)):
                self._x += self.stepSize
                self.checkEvent()

    def checkEvent(self):
        for e in self.parent.childList:
            if isinstance(e, Door):
                if e.isEnter(self):
                    break
