# -*- coding: utf-8 -*-


from scenario import *

scenario = Scenario()


class Editer(object):
    def __init__(self):
        super(Editer, self).__init__()
        self._currentScene = scenario.getScenes(0)

    def createScene(self, name):
        scene = scenario.addScene(name)
        self.currentScene = scene

    def insertPic(self, url):
        self.currentScene.addPicture(url)

    @property
    def currentScene(self):
        return self._currentScene
