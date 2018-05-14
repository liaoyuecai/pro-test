# -*- coding: utf-8 -*-

from region import *


class Scene(object):
    def __init__(self, name):
        super(Scene, self).__init__()
        self.regions = []
        self._name = name

    def addPicture(self, img):
        pic = Picture(img)
        self.regions.append(pic)

    def getRegions(self):
        return self.regions

    # 查找选中元素,没有则选中的是当前场景
    def findSelect(self, point):
        region = self
        # 倒序循环
        for r in reversed(self.regions):
            region = r.click(point)
            if region:
                region.select()
                break
        return region

    def click(self, point):
        pass

    def menu(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
