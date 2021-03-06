# -*- coding: utf-8 -*-

from region import *


class Scene(object):
    def __init__(self, name):
        super(Scene, self).__init__()
        self.regions = []
        self._name = name

    def addPicture(self, url):
        pic = Picture(url)
        self.regions.append(pic)

    def getRegions(self):
        return self.regions

    def draw(self, p):
        for region in self.regions:
            region.draw(p)

    # 查找选中元素,没有则选中的是当前场景
    def findSelect(self, point):
        re = self
        select = True
        # 倒序循环
        for r in reversed(self.regions):
            region = r.click(point, select)
            if region:
                re = region
                self.regions.remove(region)
                self.regions.append(region)
                select = False
        return re

    # def click(self, point):
    #     pass

    def menu(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
