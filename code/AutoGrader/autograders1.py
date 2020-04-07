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


class Ui_AutograderS1(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AutograderS2()
        self.ui.setupUi(self.window)
        self.window.show()
    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)
    def browse(self):
        self.openFile()
    def openFile(self):
        fileName = QFileDialog.getOpenFileName()
        path = fileName[0]
        self.label.setText(path)
        
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
        self.runButton.clicked.connect(self.download)        
        self.runButton.clicked.connect(self.openWindow)

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(90, 400, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.resetButton.setObjectName("resetButton")
        self.groundTruths = QtWidgets.QComboBox(self.centralwidget)
        self.groundTruths.setGeometry(QtCore.QRect(170, 181, 261, 31))
        self.groundTruths.setObjectName("groundTruths")
        self.groundTruths.addItem("")
        self.groundTruths.addItem("2015 Groundtruths")
        self.groundTruths.addItem("2016 Groundtruths")
        self.groundTruths.addItem("2017 Groundtruths")
        self.groundTruths.addItem("2018 Groundtruths")    
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(450, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.browse)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        self.groundTruthLabel.setText(_translate("AutograderS1", "Ground Truths"))
        self.algorithmLabel.setText(_translate("AutograderS1", "Output File"))
        self.runButton.setText(_translate("AutograderS1", "Run"))
        self.resetButton.setText(_translate("AutograderS1", "Reset"))
        self.browseButton.setText(_translate("AutograderS1", "Browse"))
        self.label.setText(_translate("AutograderS1", ""))
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
