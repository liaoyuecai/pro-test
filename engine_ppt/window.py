# -*- coding: utf-8 -*-


import sys
import cPickle as pickle
from data import *

from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    filePath = None

    def __init__(self):
        super(Window, self).__init__()
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))

    def initMenu(self):
        # textEdit = QtGui.QTextEdit()
        # self.setCentralWidget(textEdit)

        # exitAction = QtGui.QAction(QtGui.QIcon('3.bmp'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(self.close)
        #
        # self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        saveAction = QtGui.QAction('保存', self)
        fileMenu.addAction(saveAction)
        fileMenu.triggered.connect(self.saveFile)

        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAction)
        #
        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    def initBody(self):
        pass
        # timer = QtCore.QTimer()
        # timer.setInterval(1000)
        # timer.start()
        # QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"), win, QtCore.SLOT("update()"))

    def saveFile(self):
        if self.filePath:
            self.saveToFile(self.filePath)
        else:
            self.filePath = self.getSaveFileName()
            if self.filePath:
                self.saveToFile(self.filePath)
            else:
                return

    def saveToFile(self, url):
        file = open(url, 'w')
        # pickle.dump(summer, file)

    def getSaveFileName(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save File", '', '.ds')
        return filename


def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.initMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
