# -*- coding: utf-8 -*-

class Object(object):
    list = []

    def __init__(self, name=None):
        super(Object, self).__init__()
        self._name = name

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        self._sequence = sequence

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def addChild(self, child):
        self.list.append(child)

    def removeChild(self, child):
        sequence = child.sequence
        self.list.remove(child)
        for i in range(sequence, len(self.list)):
            self.list[i].sequence -= 1


class GameData(Object):
    title = None
    seq = 1

    def __init__(self):
        super(GameData, self).__init__()
        timerShaftName = '未命名' + bytes(self.seq)
        self.list.append(timerShaftName)

    def addChild(self, childName=None):
        if childName:
            self.list.append(TimerShaft(childName))
        else:
            childName = '未命名' + bytes(self.seq)
            self.list.append(TimerShaft(childName))

    def removeChild(self, child):
        if child.sequence == 0:
            print ('初始时间轴不能删除')
            return
        sequence = child.sequence
        self.list.remove(child)
        for i in range(sequence, len(self.list)):
            self.list[i].sequence -= 1


# 时间轴
class TimerShaft(Object):

    def __init__(self, name):
        super(TimerShaft, self).__init__()
        self.name = name


# 帧
class Frame(Object):
    def __init__(self, name):
        super(Frame, self).__init__()
        self.name = name

    def addCoverage(self, chlid):
        # 背景继承
        if len(self.coverages) > 0:
            chlid.background = self.coverages[-1].background
        self.list.append(chlid)


# 图层
class Coverage(Object):
    background = None

    def __init__(self, name):
        super(Coverage, self).__init__()
        self.name = name

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background


class Element(Object):
    def __init__(self, x, y, width, high, name):
        super(Element, self).__init__()
        self._x = x
        self._y = y
        self._scalaX = 1
        self._scalaY = 1
        self._width = width
        self._high = high
        self._name = name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def scalaX(self):
        return self._scalaX

    @property
    def scalaY(self):
        return self._scalaY

    @property
    def width(self):
        return self._scalaX * self._width

    @property
    def high(self):
        return self._scalaY * self._high

    @scalaX.setter
    def scalaX(self, scalaX):
        self._scalaX = scalaX

    @scalaY.setter
    def scalaY(self, scalaY):
        self._scalaY = scalaY


gameData = GameData()
