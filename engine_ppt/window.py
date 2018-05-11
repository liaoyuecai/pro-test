# -*- coding: utf-8 -*-


import sys
import cPickle as pickle
from data import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))


class Record(object):
    def __init__(self):
        super(Record, self).__init__()

    currentTimeAxis = 1
    currentTimerShaft = gameData.getChild(0)
    sumTimeAxis = None
    showTimeAxis = None
    currentCoverage = None


record = Record()


class Window(QMainWindow):
    filePath = None
    body = None

    def __init__(self):
        super(Window, self).__init__()

    def initMenu(self):
        # 菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction('保存', self.saveFile)
        insertMenu = menubar.addMenu('插入')
        insertMenu.addAction('新建图层', self.insertCoverage)

        # 工具栏
        toolbar = self.addToolBar('tool')
        record.sumTimeAxis = toolbar.addAction(('[时间轴(' + bytes(gameData.getChildrenLen()) + ')：'))
        toolbar.addAction(QIcon('2.bmp'), '前进', self._leftTimeAxis)
        record.showTimeAxis = toolbar.addAction(
            (bytes(record.currentTimeAxis) + '(' + record.currentTimerShaft.name + ')'))
        toolbar.addAction(QIcon('2.bmp'), '后退', self._rightTimeAxis)
        toolbar.addAction('选择时间轴]', self.choseTimeAxis)

        record.sumTimeAxis = toolbar.addAction(('[图层(' + bytes(gameData.getChildrenLen()) + ')：'))
        toolbar.addAction(QIcon('2.bmp'), '前进', self._leftTimeAxis)
        record.showTimeAxis = toolbar.addAction(
            (bytes(record.currentTimeAxis) + '(' + record.currentTimerShaft.name + ')'))
        toolbar.addAction(QIcon('2.bmp'), '后退', self._rightTimeAxis)
        toolbar.addAction('选择时间轴]', self.choseTimeAxis)

        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('engine ppt')
        self.center()
        self.show()

    def _leftTimeAxis(self):
        if record.currentTimeAxis > 1:
            record.currentTimeAxis -= 1
            record.showTimeAxis.setText(bytes(record.currentTimeAxis))
            record.currentTimerShaft = gameData.getChild((record.currentTimeAxis - 1))

    def _rightTimeAxis(self):
        if record.currentTimeAxis < gameData.getChildrenLen():
            record.currentTimeAxis += 1
            record.showTimeAxis.setText(bytes(record.currentTimeAxis))
            record.currentTimerShaft = gameData.getChild((record.currentTimeAxis - 1))

    def insertCoverage(self):
        cl_win = QDialog(self)
        cl_win.resize(200, 40)
        grid = QGridLayout()
        grid.addWidget(QLabel('图层名称:', parent=cl_win), 0, 0, 1, 1)
        coverageName = QLineEdit(parent=cl_win)
        grid.addWidget(coverageName, 0, 1, 1, 1)
        buttonBox = QDialogButtonBox(parent=cl_win)
        buttonBox.setOrientation(Qt.Horizontal)
        buttonBox.addButton('确定', 0)
        buttonBox.addButton('取消', 1)
        buttonBox.accepted.connect(lambda: self.saveCoverage(coverageName, cl_win))
        buttonBox.rejected.connect(cl_win.close)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        # spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        cl_win.setLayout(layout)
        cl_win.setWindowTitle('插入图层')
        cl_win.exec_()

    def saveCoverage(self, coverageName, win):
        if coverageName.text():
            record.currentTimerShaft.addChild(Coverage(coverageName.text()))
        else:
            record.currentTimerShaft.addChild(Coverage('未命名'))
        win.close()

    def choseTimeAxis(self):
        cl_win = QDialog(self)
        cl_win.resize(200, 40)
        grid = QGridLayout()
        grid.addWidget(QLabel('选择时间轴:', parent=cl_win), 0, 0, 1, 1)
        combo = QComboBox(self)
        for child in gameData.getChildren():
            combo.addItem(child.name)
        grid.addWidget(combo, 0, 1, 1, 1)
        buttonBox = QDialogButtonBox(parent=cl_win)
        # 设置为水平方向
        buttonBox.setOrientation(Qt.Horizontal)
        # 确定和取消两个按钮
        buttonBox.addButton('确定', 0)
        buttonBox.addButton('取消', 1)
        # 确定
        buttonBox.accepted.connect(lambda: self.selectTimeAxis(combo, cl_win))
        # 取消
        buttonBox.rejected.connect(cl_win.close)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(buttonBox)
        cl_win.setLayout(layout)
        cl_win.setWindowTitle('选择时间轴')
        cl_win.exec_()

    def initBody(self):
        self.body = BodyQWidget()
        self.setCentralWidget(self.body)
        self.body.show()

    def selectTimeAxis(self, combo, win):
        self.changeTimeAxis(combo.currentIndex())
        win.close()

    def changeTimeAxis(self, seq):
        record.currentTimeAxis = seq + 1
        record.showTimeAxis.setText(bytes((seq + 1)))
        record.currentTimerShaft = gameData.getChild((seq - 1))

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
        pickle.dump(gameData, file)

    def getSaveFileName(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", '', '.ds')
        return filename


class BodyQWidget(QWidget):
    def __init__(self):
        super(BodyQWidget, self).__init__()

    def paintEvent(self, event):
        coverages = record.currentTimerShaft.getChildren()
        for chlid in coverages:
            self.drawCoverage(chlid)

    def drawCoverage(self, coverage):
        elements = coverage.getChildren()
        for chlid in elements:
            self.drawElement(chlid)

    def drawElement(self, element):
        element._show(widget=self)

    def mousePressEvent(self, event):
        button = event.button()
        if button == 1:
            print(bytes(event.x()) + '==' + bytes(event.y()))
        elif button == 2:
            active = record.currentCoverage.choseActive(event)
            active.mouseRight(self, event)


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.initMenu()
    win.initBody()
    timer = QTimer()
    timer.setInterval(11)
    timer.start()
    QObject.connect(timer, SIGNAL("timeout()"), win, SLOT("update()"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
