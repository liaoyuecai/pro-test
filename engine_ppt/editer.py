# -*- coding: utf-8 -*-


from scenario import *


class Editer(object):
    fileSeq = 1

    def __init__(self):
        super(Editer, self).__init__()
        self._scenarios = []
        self._currentScenario = Scenario('未命名')
        self._scenarios.append(self._currentScenario)
        self._currentScene = self._currentScenario.getScene(0)

    def insertScenarios(self, name):
        index = self._scenarios.index(self._currentScenario)
        scenarios = Scenario(name)
        self._scenarios.insert(index, scenarios)

    def insertScene(self, name):
        self._currentScenario.insertScene(self._currentScene, name)

    def insertPic(self, url):
        self.currentScene.addPicture(url)

    @property
    def currentScenario(self):
        return self._currentScenario

    def changeScenario(self, seq):
        self._currentScenario = self._scenarios[seq]

    @property
    def scenarios(self):
        return self._scenarios

    @property
    def currentScene(self):
        return self._currentScene

    def changeScene(self, seq):
        self._currentScene = self._currentScene.getScene(seq)


def QString2PyString(s):
    return unicode(s.toUtf8(), 'utf-8', 'ignore')
