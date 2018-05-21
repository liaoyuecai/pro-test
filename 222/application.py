# -*- coding: utf-8 -*-
from scene import *


# class Application(object):
#     def __init__(self, title, iconUrl, width, height):
#         super(Application, self).__init__()
#         self.interface = Interface(title, iconUrl, width, height)
#
#     def setProtagonist(self, protagonist):
#         self.interface.setProtagonist(protagonist)
#
#     def setCoreScene(self, scene):
#         self.interface.setCoreScene(scene)


class Application(QWidget):
    def __init__(self, title, iconUrl, width, height):
        super(Application, self).__init__()
        self.currentScene = None
        self.mainScene = None
        self.protagonist = None
        self.setFixedSize(width, height)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconUrl))
        self.scenes = []
        self.scenesDict = {}

    def setProtagonist(self, protagonist):
        self.protagonist = protagonist

    def setMainScene(self, scene):
        self.mainScene = scene
        self.currentScene = scene

    def addScene(self, scene):
        self.scenes.append(scene)
        self.scenesDict[scene.name] = self.scenes.index(scene)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.role.goLeft()
        elif event.key() == Qt.Key_Right:
            self.role.goRight()
        elif event.key() == Qt.Key_Up:
            self.role.goUp()
        elif event.key() == Qt.Key_Down:
            self.role.goDown()
