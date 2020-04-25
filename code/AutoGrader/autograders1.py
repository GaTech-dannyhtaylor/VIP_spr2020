# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autograders1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from autograders2 import Ui_AutograderS2
from truepositive import Ui_TruePositiveWindow

import runautograder
import dataclass


class Ui_AutograderS1(object):
    def openWindow(self):
        if (self.label.text() == "" or self.groundlabel.text() == ""):
            return
        self.download()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AutograderS2()
        # algoOutput = runautograder.run("User_output.csv", "GT")

        self.ui.setupUi(self.window)
        self.window.show()
        algoOutput = runautograder.run(self.label.text(), self.groundlabel.text())
        self.ui.changeScore(str(round(algoOutput[0], 2)))
        self.ui.changeTP(str(algoOutput[1]))
        self.ui.changeTN(str(algoOutput[2]))
        self.ui.changeFP(str(algoOutput[3]))
        self.ui.changeFN(str(algoOutput[4]))


    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 1
            self.progressBar.setValue(self.completed)

    def openFile(self):
        fileName = QFileDialog.getOpenFileName()
        path = fileName[0]
        self.label.setText(path)

    def openFolder(self):
        fileName = QFileDialog.getExistingDirectory()
        self.groundlabel.setText(fileName)


    def setupUi(self, AutograderS1):
        AutograderS1.setObjectName("AutograderS1")
        AutograderS1.resize(800, 600)
        AutograderS1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(AutograderS1)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(36)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.groundTruthLabel = QtWidgets.QLabel(self.centralwidget)
        self.groundTruthLabel.setGeometry(QtCore.QRect(20, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.groundTruthLabel.setFont(font)
        self.groundTruthLabel.setObjectName("groundTruthLabel")
        self.algorithmLabel = QtWidgets.QLabel(self.centralwidget)
        self.algorithmLabel.setGeometry(QtCore.QRect(20, 230, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.algorithmLabel.setFont(font)
        self.algorithmLabel.setObjectName("algorithmLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 370, 641, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(570, 400, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.runButton.setFont(font)
        self.runButton.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.runButton.setObjectName("runButton")
        self.runButton.clicked.connect(self.openWindow)

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(90, 400, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.resetButton.setObjectName("resetButton")
        self.groundTruths = QtWidgets.QLabel(self.centralwidget)
        self.groundTruths.setGeometry(QtCore.QRect(170, 181, 261, 31))
        self.groundTruthBrowseButton = QtWidgets.QPushButton(self.centralwidget)
        self.groundTruthBrowseButton.setGeometry(QtCore.QRect(450, 180, 91, 41))
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(450, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.openFile)
        self.groundTruthBrowseButton.setFont(font)
        self.browseButton.setFont(font)
        self.groundTruthBrowseButton.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.groundTruthBrowseButton.setObjectName("groundBrowseButton")
        self.groundTruthBrowseButton.clicked.connect(self.openFolder)

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 240, 261, 31))
        self.groundlabel = QtWidgets.QLabel(self.centralwidget)
        self.groundlabel.setGeometry(QtCore.QRect(170, 180, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groundlabel.setFont(font)
        self.groundlabel.setObjectName("groundlabel")
        AutograderS1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutograderS1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        AutograderS1.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(AutograderS1)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHome.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(AutograderS1)
        QtCore.QMetaObject.connectSlotsByName(AutograderS1)

    def retranslateUi(self, AutograderS1):
        _translate = QtCore.QCoreApplication.translate
        AutograderS1.setWindowTitle(_translate("AutograderS1", "AutograderS1"))
        self.titleLabel.setText(_translate("AutograderS1", "3D Point Cloud Autograder"))
        self.groundTruthLabel.setText(_translate("AutograderS1", "Ground Truth"))
        self.algorithmLabel.setText(_translate("AutograderS1", "Algorithm Input"))
        self.runButton.setText(_translate("AutograderS1", "Run"))
        self.resetButton.setText(_translate("AutograderS1", "Reset"))
        self.browseButton.setText(_translate("AutograderS1", "Browse"))
        self.groundTruthBrowseButton.setText(_translate("AutograderS1", "Browse"))
        self.label.setText(_translate("AutograderS1", ""))
        self.groundlabel.setText(_translate("AutograderS1", ""))
        self.menuHome.setTitle(_translate("AutograderS1", "Home"))
        self.actionHelp.setText(_translate("AutograderS1", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutograderS1 = QtWidgets.QMainWindow()
    ui = Ui_AutograderS1()
    ui.setupUi(AutograderS1)
    AutograderS1.show()
    sys.exit(app.exec_())
