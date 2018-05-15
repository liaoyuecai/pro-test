# -*- coding: utf-8 -*-

from scene import *


class Scenario(object):
    def __init__(self):
        super(Scenario, self).__init__()
        self.scenes = []
        self.scenes.append(Scene('未命名'))

    def addScene(self, name):
        scene = Scene(name)
        self.scenes.append(scene)
        return scene

    def insertScene(self, current, name):
        index = self.scenes.index(current)
        scene = Scene(name)
        self.scenes.insert(index, scene)
        return scene

    def getScenes(self, seq):
        return self.scenes[seq]
