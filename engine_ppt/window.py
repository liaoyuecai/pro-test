# -*- coding: utf-8 -*-

import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from editer import *

QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))

editer = Editer()
editer.insertPic('pic/1.png')
editer.insertPic('pic/2.png')

data_directory = 'F:/PycharmProjects/pro-test/engine_ppt/'


class Window(QMainWindow):
    fileSeq = 1

    def __init__(self):
        super(Window, self).__init__()

    def init(self):
        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('engine ppt')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.initMenu()
        self.initToolBar()
        self.initBody()
        self.show()

    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('插入')
        fileMenu.addAction('插入图片', self.insertPic)
        pass

    def initToolBar(self):
        pass

    def initBody(self):
        body = BodyQWidget()
        self.setCentralWidget(body)
        body.show()

    def insertPic(self):
        filePath = QFileDialog.getOpenFileName(self, "Open File", '', 'Images (*.*)')
        if filePath:
            file = open(filePath, 'r')
            self.saveFile('pic/', filePath.split('.')[-1], file.read())
            file.close()

    def saveFile(self, directory, suffix, data):
        directory = data_directory + directory
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = directory + bytes(self.fileSeq) + ',' + suffix
        file = open(path, 'w')
        file.write(data)
        file.close()


class BodyQWidget(QWidget):
    def __init__(self):
        super(BodyQWidget, self).__init__()

    def paintEvent(self, event):
        scene = editer.currentScene
        regions = scene.getRegions()
        painter = QPainter()
        painter.begin(self)
        for region in regions:
            region.draw(painter)
        painter.end()


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.init()
    timer = QTimer()
    timer.setInterval(11)
    timer.start()
    QObject.connect(timer, SIGNAL("timeout()"), win, SLOT("update()"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
