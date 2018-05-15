# -*- coding: utf-8 -*-

import sys, os, shutil, cPickle
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

    def init(self):
        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('engine ppt')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.initMenu()
        self.initToolBar()
        # self.initBody()
        self.show()

    def initMenu(self):
        self.menu = self.menuBar()
        fileMenu = self.menu.addMenu('文件')
        fileMenu.addAction('新建', self.newPro)
        fileMenu.addAction('打开', self.open)
        fileMenu.addAction('保存', self.save)

    def initToolBar(self):
        self.toolbar = self.addToolBar('tool')

    def initBody(self):
        insertMenu = self.menu.addMenu('插入')
        insertMenu.addAction('插入图片', self.insertPic)
        self.toolbar.addWidget(QLabel('世界线：'))
        combo = QComboBox(self)
        combo.addItem('1')
        combo.addItem('2')
        self.toolbar.addWidget(combo)
        self.body = BodyQWidget(self.editer)
        self.setCentralWidget(self.body)
        self.body.show()

    def newPro(self):
        if self.data_directory:
            grid = QGridLayout()
            grid.addWidget(QLabel('是否放弃当前编辑?'))
            box = DialogBox(grid, self.createPro)
            box.show()
        else:
            self.createPro()

    def open(self):
        self.data_directory = QFileDialog.getExistingDirectory(self, "选择文件夹", '')
        if self.data_directory:
            path = self.data_directory + '/edit.ds'
            if not os.path.exists(path):
                grid = QGridLayout()
                grid.addWidget(QLabel('加载失败，edit.ds 文件不存在' ))
                box = DialogBox(grid, self.createPro)
                box.show()
            else:
                try:
                    file = open(path, 'rb')
                    self.editer = cPickle.load(file)
                    file.close()
                    self.initBody()
                    self.update()
                except RuntimeError:
                    grid = QGridLayout()
                    grid.addWidget(QLabel('edit.ds 文件被破坏', ))
                    box = DialogBox(grid, self.createPro)
                    box.show()

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
    def __init__(self, grid, call=None, title='警告', *args):
        super(DialogBox, self).__init__()
        self.setWindowTitle(title)
        buttonBox = QDialogButtonBox(parent=self)
        # 设置为水平方向
        buttonBox.setOrientation(Qt.Horizontal)
        if call is None:
            buttonBox.addButton('确定', 0)
            buttonBox.accepted.connect(self.close)
        else:
            # 确定和取消两个按钮
            buttonBox.addButton('确定', 0)
            buttonBox.addButton('取消', 1)
            # 确定
            buttonBox.accepted.connect(lambda: call(self, *args))
            # 取消
            buttonBox.rejected.connect(self.close)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(buttonBox)
        self.setLayout(layout)


class BodyQWidget(QWidget):
    def __init__(self, editer):
        super(BodyQWidget, self).__init__()
        self.mouse = None
        self.mouse_x = None
        self.mouse_y = None
        self.mouseRegion = None
        self.editer = editer

    def paintEvent(self, event):
        scene = self.editer.currentScene
        regions = scene.getRegions()
        painter = QPainter()
        painter.begin(self)
        for region in regions:
            region.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        button = event.button()
        region = self.editer.currentScene.findSelect(event.pos())
        if button == Qt.LeftButton:
            if not isinstance(region, Scene):
                self.update()
                self.mouseRegion = region
                self.mouse_x = event.x() - region.x
                self.mouse_y = event.y() - region.y
        elif button == Qt.RightButton:
            print('点击右键')
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
    timer.setInterval(1000)
    timer.start()
    # QObject.connect(timer, SIGNAL("timeout()"), win, SLOT("update()"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
