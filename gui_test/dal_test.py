# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np

from PyQt4 import QtGui, QtCore


class MultiInPutDialog(QtGui.QDialog):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)

        self.resize(100, 80)

        self.setWindowTitle('Input')

        self.setWindowIcon(QtGui.QIcon('td.png'))

        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel('Data Rows:', parent=self), 0, 0, 1, 1)

        self.num_R = QtGui.QLineEdit(parent=self)

        grid.addWidget(self.num_R, 0, 1, 1, 1)

        grid.addWidget(QtGui.QLabel('Data Cols:', parent=self), 1, 0, 1, 1)

        self.num_C = QtGui.QLineEdit(parent=self)

        grid.addWidget(self.num_C, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        # 设置为水平方向
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # 确定和取消两个按钮
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        # 确定
        buttonBox.accepted.connect(self.accept)
        # 取消
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()

        layout.addLayout(grid)

        spacerItem = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        layout.addItem(spacerItem)

        layout.addWidget(buttonBox)

        self.setLayout(layout)

        # -------------------Close Event Method----------------------

        def closeEvent(self, event):

            reply = QtGui.QMessageBox.question(self, 'Close Message',

                                               "Are you sure to quit?", QtGui.QMessageBox.Yes |

                                               QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:

                event.accept()

            else:

                event.ignore()


app = QtGui.QApplication([])

dialog = MultiInPutDialog()

if dialog.exec_():
    hs = int(dialog.num_R.text())

    ls = int(dialog.num_C.text())

print hs

print ls
