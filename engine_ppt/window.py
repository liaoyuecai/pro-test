# -*- coding: utf-8 -*-


import sys
import cPickle as pickle
from data import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Window(QMainWindow):
    filePath = None

    currentTimeAxis = 1
    currentTimerShaft = gameData.getChild(0)
    sumTimeAxis = None
    showTimeAxis = None

    def __init__(self):
        super(Window, self).__init__()
        QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))
        # btn =  QPushButton('111',self)
        # btn.showMenu()


    def initMenu(self):
        # textEdit = QtGui.QTextEdit()
        # self.setCentralWidget(textEdit)

        # exitAction = QtGui.QAction(QtGui.QIcon('3.bmp'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(self.close)
        #
        # self.statusBar()
        # 菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction('保存', self.saveFile)

        # 工具栏
        toolbar = self.addToolBar('tool')
        self.sumTimeAxis = toolbar.addAction(('时间轴(' + bytes(gameData.getChildrenLen()) + ')：'))
        toolbar.addAction(QIcon('2.bmp'), '前进', self._leftTimeAxis)
        self.showTimeAxis = toolbar.addAction((bytes(self.currentTimeAxis) + '(' + self.currentTimerShaft.name + ')'))
        toolbar.addAction(QIcon('2.bmp'), '后退', self._rightTimeAxis)
        toolbar.addAction('选择时间轴', self.choseTimeAxis)


        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('engine ppt')
        self.center()
        self.show()

    def _leftTimeAxis(self):
        if self.currentTimeAxis > 1:
            self.currentTimeAxis -= 1
            self.showTimeAxis.setText(bytes(self.currentTimeAxis))
            self.currentTimerShaft = gameData.getChild((self.currentTimeAxis - 1))

    def _rightTimeAxis(self):
        if self.currentTimeAxis < gameData.getChildrenLen():
            self.currentTimeAxis += 1
            self.showTimeAxis.setText(bytes(self.currentTimeAxis))
            self.currentTimerShaft = gameData.getChild((self.currentTimeAxis - 1))

    def choseTimeAxis(self):
        cl_win = QDialog(self)
        cl_win.resize(200, 200)
        grid = QGridLayout()
        btn = QPushButton('111', cl_win)
        btn.showMenu()
        grid.addWidget(btn, 1, 0, 1, 1)
        cl_win.setLayout(grid)
        cl_win.setWindowTitle('main windows')
        cl_win.exec_()



    def initBody(self):
        pass

    def center(self):  # 主窗口居中显示函数
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

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
        filename = QFileDialog.getSaveFileName(self, "Save File", '', '.ds')
        return filename



def main():
    app = QApplication(sys.argv)
    win = Window()
    win.initMenu()
    timer = QTimer()
    timer.setInterval(11)
    timer.start()
    QObject.connect(timer, SIGNAL("timeout()"), win, SLOT("update()"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
