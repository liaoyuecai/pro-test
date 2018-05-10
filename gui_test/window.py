# -*- coding: utf-8 -*-

"""
This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar and a central widget.
"""

import sys
from PyQt4 import QtGui,QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))
        self.initUI()

    def initUI(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon('3.bmp'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('开始')

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
