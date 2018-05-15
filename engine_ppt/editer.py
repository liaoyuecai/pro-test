# -*- coding: utf-8 -*-


from scenario import *


class Editer(object):
    fileSeq = 1

    def __init__(self):
        super(Editer, self).__init__()
        self._scenarios = []
        self._currentScenario = Scenario()
        self._scenarios.append(self._currentScenario)
        self._currentScene = self.scenario.getScenes(0)

    def createScene(self, name):
        scene = self.scenario.addScene(name)
        self.currentScene = scene

    def insertScene(self, name):
        self.scenario.insertScene(self._currentScene, name)

    def insertPic(self, url):
        self.currentScene.addPicture(url)

    @property
    def currentScene(self):
        return self._currentScene

    @property
    def currentScene(self):
        return self._currentScene


def QString2PyString(qStr):
    return unicode(qStr.toUtf8(), 'utf-8', 'ignore')
