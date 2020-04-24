# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'falsepositive.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FalsePositiveWindow(object):
    def setupUi(self, FalsePositiveWindow):
        FalsePositiveWindow.setObjectName("FalsePositiveWindow")
        FalsePositiveWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FalsePositiveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FalsePositiveLabel = QtWidgets.QLabel(self.centralwidget)
        self.FalsePositiveLabel.setGeometry(QtCore.QRect(360, 140, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.FalsePositiveLabel.setFont(font)
        self.FalsePositiveLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.FalsePositiveLabel.setObjectName("FalsePositiveLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(36)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.falsePositiveTable = QtWidgets.QTableWidget(self.centralwidget)
        self.falsePositiveTable.setGeometry(QtCore.QRect(310, 200, 241, 301))
        self.falsePositiveTable.setRowCount(12)
        self.falsePositiveTable.setColumnCount(2)
        self.falsePositiveTable.setObjectName("falsePositiveTable")
        item = QtWidgets.QTableWidgetItem()
        self.falsePositiveTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.falsePositiveTable.setItem(0, 1, item)
        FalsePositiveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FalsePositiveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FalsePositiveWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FalsePositiveWindow)
        self.statusbar.setObjectName("statusbar")
        FalsePositiveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FalsePositiveWindow)
        QtCore.QMetaObject.connectSlotsByName(FalsePositiveWindow)

    def retranslateUi(self, FalsePositiveWindow):
        _translate = QtCore.QCoreApplication.translate
        FalsePositiveWindow.setWindowTitle(_translate("FalsePositiveWindow", "MainWindow"))
        self.FalsePositiveLabel.setText(_translate("FalsePositiveWindow", "False Positive"))
        self.titleLabel.setText(_translate("FalsePositiveWindow", "3D Point Cloud Autograder"))
        __sortingEnabled = self.falsePositiveTable.isSortingEnabled()
        self.falsePositiveTable.setSortingEnabled(False)
        item = self.falsePositiveTable.item(0, 0)
        item.setText(_translate("FalsePositiveWindow", "Sign"))
        item = self.falsePositiveTable.item(0, 1)
        item.setText(_translate("FalsePositiveWindow", "Score"))
        self.falsePositiveTable.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FalsePositiveWindow = QtWidgets.QMainWindow()
    ui = Ui_FalsePositiveWindow()
    ui.setupUi(FalsePositiveWindow)
    FalsePositiveWindow.show()
    sys.exit(app.exec_())
