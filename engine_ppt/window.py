# -*- coding: utf-8 -*-

import cPickle
import os
import shutil
import sys

from editer import *

QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.body = None
        self.menu = None
        self.toolbar = None
        self.editer = None
        self.data_directory = None
        self.scenarioCombo = None
        self.sceneCombo = None
        self.insertMenu = None

    def init(self):
        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('engine ppt')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.initMenu()
        self.initToolBar()
        self.show()

    def initMenu(self):
        self.menu = self.menuBar()
        fileMenu = self.menu.addMenu('文件')
        fileMenu.addAction('新建', self.newPro)
        fileMenu.addAction('打开', self.open)
        fileMenu.addAction('保存', self.save)

    def initToolBar(self):
        self.toolbar = self.addToolBar('tool')

    def perfectMenu(self):
        if self.insertMenu is None:
            self.insertMenu = self.menu.addMenu('插入')
            self.insertMenu.addAction('插入世界线', self.toInsertScenario)
            self.insertMenu.addAction('插入场景', self.toInsertScene)
            self.insertMenu.addAction('插入图片', self.insertPic)

    def toInsertScenario(self):
        box = DialogBox()
        box.initInputBox(self.insertScenario, '输入世界线名称')

    def toInsertScene(self):
        box = DialogBox()
        box.initInputBox(self.insertScene, '输入场景名称')

    def insertScene(self, box, name):
        if name:
            self.editer.insertScene(name)
            self.sceneCombo.addItem(name)
            self.sceneCombo.setCurrentIndex(self.sceneCombo.count() - 1)
            self.body.update()
            box.close()
        else:
            warn = DialogBox()
            warn.initWarnBox('请输入场景名称')

    def insertScenario(self, box, name):
        if name:
            index = self.editer.insertScenarios(name)
            self.scenarioCombo.insertItem(index, name)
            self.scenarioCombo.setCurrentIndex(index)
            self.body.update()
            box.close()
        else:
            warn = DialogBox()
            warn.initWarnBox('请输入世界线名称')

    def perfectToolBar(self):
        self.toolbar.clear()
        self.toolbar.addWidget(QLabel('世界线：'))
        self.scenarioCombo = QComboBox(self)
        self.scenarioCombo.setMinimumContentsLength(20)
        self.sceneCombo = QComboBox(self)
        self.sceneCombo.setMinimumContentsLength(20)
        for s in self.editer.scenarios:
            self.scenarioCombo.addItem(s.name)
        self.connect(self.scenarioCombo, SIGNAL('currentIndexChanged(int)'), self.changeScenario)
        self.toolbar.addWidget(self.scenarioCombo)
        for s in self.editer.currentScenario.getScenes():
            self.sceneCombo.addItem(s.name)
        self.toolbar.addWidget(QLabel(' | 场景：'))
        self.connect(self.sceneCombo, SIGNAL('currentIndexChanged(int)'), self.changeScene)
        self.toolbar.addWidget(self.sceneCombo)

    def resetSceneCombo(self):
        self.sceneCombo.clear()
        for s in self.editer.currentScenario.getScenes():
            self.sceneCombo.addItem(s.name)

    def toEditScenarioName(self):
        box = DialogBox()
        box.initInputBox(self.editScenarioName, '输入世界线名称')

    def toEditSceneName(self):
        box = DialogBox()
        box.initInputBox(self.editSceneName, '输入场景名称')

    def editScenarioName(self, box, name):
        if name:
            self.scenarioCombo.setItemText(self.scenarioCombo.currentIndex(), name)
            self.editer.currentScenario.name = QString2PyString(name)
        box.close()

    def editSceneName(self, box, name):
        if name:
            self.sceneCombo.setItemText(self.sceneCombo.currentIndex(), name)
            self.editer.currentScene.name = QString2PyString(name)
        box.close()

    def changeScenario(self, seq):
        self.editer.changeScenario(seq)
        self.resetSceneCombo()
        self.update()

    def changeScene(self, seq):
        self.editer.changeScene(seq)
        self.update()

    def initBody(self):
        self.perfectMenu()
        self.perfectToolBar()
        self.body = BodyQWidget(self)
        self.setCentralWidget(self.body)
        self.body.show()

    def newPro(self):
        if self.data_directory:
            box = DialogBox()
            box.initChoseBox(self.createPro, '是否放弃当前编辑?')
        else:
            self.createPro()

    def open(self):
        self.data_directory = QFileDialog.getExistingDirectory(self, "选择文件夹", '')
        if self.data_directory:
            path = self.data_directory + '/edit.ds'
            if not os.path.exists(path):
                self.data_directory = None
                box = DialogBox()
                box.initWarnBox('加载失败，edit.ds 文件不存在')
            else:
                try:
                    file = open(path, 'rb')
                    self.editer = cPickle.load(file)
                    file.close()
                    self.initBody()
                    self.update()
                except RuntimeError:
                    self.data_directory = None
                    box = DialogBox()
                    box.initWarnBox('edit.ds 文件被破坏')

    def createPro(self, box=None):
        self.data_directory = QFileDialog.getExistingDirectory(self, "选择文件夹", '')
        if self.data_directory:
            self.editer = Editer()
            self.initBody()
            self.save()
            self.update()
        if box:
            box.close()

    def save(self):
        if self.data_directory and self.editer:
            file = open(self.data_directory + '/edit.ds', 'wb')
            cPickle.dump(self.editer, file)
            file.close()

    def insertPic(self):
        filePath = QFileDialog.getOpenFileName(self, "插入图片", '', 'Images (*.*)')
        if filePath:
            directory = self.data_directory + '/pic/'
            if not os.path.exists(directory):
                os.makedirs(QString2PyString(directory))
            path = directory + bytes(self.editer.fileSeq) + '.' + filePath.split('.')[-1]
            shutil.copyfile(filePath, path)
            self.editer.insertPic(path)
            self.editer.fileSeq += 1
            self.body.update()


class DialogBox(QDialog):
    def __init__(self):
        super(DialogBox, self).__init__()
        self.buttonBox = QDialogButtonBox(parent=self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def initInputBox(self, call, info, *args):
        self.setWindowTitle('请输入')
        self.buttonBox.addButton('确定', 0)
        self.buttonBox.addButton('取消', 1)
        self.grid.addWidget(QLabel(info, parent=self), 0, 0, 1, 1)
        input = QLineEdit(parent=self)
        self.grid.addWidget(input, 0, 1, 1, 1)
        self.buttonBox.accepted.connect(lambda: call(self, input.text(), *args))
        self.buttonBox.rejected.connect(self.close)
        self.show()

    def initChoseBox(self, call, info, *args):
        self.setWindowTitle('提示')
        self.buttonBox.addButton('确定', 0)
        self.buttonBox.addButton('取消', 1)
        self.buttonBox.accepted.connect(lambda: call(self, *args))
        self.buttonBox.rejected.connect(self.close)
        self.grid.addWidget(QLabel(info, parent=self))
        self.show()

    def initWarnBox(self, warn):
        self.setWindowTitle('警告')
        self.buttonBox.addButton('确定', 0)
        self.buttonBox.accepted.connect(lambda: self.close())
        self.grid.addWidget(QLabel(warn, parent=self))
        self.show()


class BodyQWidget(QWidget):
    def __init__(self, parent):
        super(BodyQWidget, self).__init__()
        self.mouse = None
        self.mouse_x = None
        self.mouse_y = None
        self.mouseRegion = None
        self.parent = parent

    def paintEvent(self, event):
        scene = self.parent.editer.currentScene
        painter = QPainter()
        painter.begin(self)
        scene.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        button = event.button()
        region = self.parent.editer.currentScene.findSelect(event.pos())
        if button == Qt.LeftButton:
            if not isinstance(region, Scene):
                self.update()
                self.mouseRegion = region
                self.mouse_x = event.x() - region.x
                self.mouse_y = event.y() - region.y
        elif button == Qt.RightButton:
            contextMenu = QMenu(self)
            contextMenu.addAction('世界线重命名', self.parent.toEditScenarioName)
            contextMenu.addAction('场景重命名', self.parent.toEditSceneName)
            contextMenu.move(event.globalPos())
            contextMenu.show()
        self.mouse = button

    def mouseMoveEvent(self, event):
        if self.mouse == Qt.LeftButton:
            if self.mouseRegion:
                self.mouseRegion.move(event.x() - self.mouse_x, event.y() - self.mouse_y)
                self.update()

    def mouseReleaseEvent(self, event):
        self.mouse = None
        self.mouseRegion = None


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.init()
    timer = QTimer()
    timer.setInterval(3000)
    timer.start()
    timer.timeout.connect(win.save)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
