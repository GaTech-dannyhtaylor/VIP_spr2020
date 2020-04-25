# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'truepositive.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dataclass

class Ui_TruePositiveWindow(object):
    def setupUi(self, TruePositiveWindow):
        TruePositiveWindow.setObjectName("TruePositiveWindow")
        TruePositiveWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TruePositiveWindow)
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
        self.TruePositiveLabel = QtWidgets.QLabel(self.centralwidget)
        self.TruePositiveLabel.setGeometry(QtCore.QRect(340, 140, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.TruePositiveLabel.setFont(font)
        self.TruePositiveLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TruePositiveLabel.setObjectName("TruePositiveLabel")
        self.TruePositiveLabel.setStyleSheet("background-color: purple")
        self.truePositiveTable = QtWidgets.QTableWidget(self.centralwidget)
        self.truePositiveTable.setGeometry(QtCore.QRect(150, 200, 502, 300))
        self.truePositiveTable.setShowGrid(True)
        self.truePositiveTable.horizontalHeader().setVisible(False)
        self.truePositiveTable.verticalHeader().setVisible(False)
        self.truePositiveTable.setRowCount(int(len(dataclass.truePositive) / 5) + 1)
        self.truePositiveTable.setColumnCount(5)
        self.truePositiveTable.setObjectName("truePositiveTable")
        item = QtWidgets.QTableWidgetItem()
        self.truePositiveTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.truePositiveTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.truePositiveTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.truePositiveTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.truePositiveTable.setItem(0, 4, item)
        print(dataclass.truePositive[0])
        for i in range(1, int(len(dataclass.truePositive) / 5) + 1):
            item = QtWidgets.QTableWidgetItem("Sign " + str(dataclass.truePositive[5 * (i - 1)]))
            self.truePositiveTable.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(str(dataclass.truePositive[5 * (i - 1) + 2]))
            self.truePositiveTable.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem(str(round(dataclass.truePositive[5 * (i - 1) + 3], 2)))
            self.truePositiveTable.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem(str(dataclass.truePositive[5 * (i - 1) + 4]))
            self.truePositiveTable.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem(str(round(dataclass.truePositive[5 * (i - 1) + 1], 2)))
            self.truePositiveTable.setItem(i, 4, item)


        TruePositiveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TruePositiveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        TruePositiveWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TruePositiveWindow)
        self.statusbar.setObjectName("statusbar")
        TruePositiveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TruePositiveWindow)
        QtCore.QMetaObject.connectSlotsByName(TruePositiveWindow)

    def retranslateUi(self, TruePositiveWindow):
        _translate = QtCore.QCoreApplication.translate
        TruePositiveWindow.setWindowTitle(_translate("TruePositiveWindow", "MainWindow"))
        self.titleLabel.setText(_translate("TruePositiveWindow", "3D Point Cloud Autograder"))
        self.TruePositiveLabel.setText(_translate("TruePositiveWindow", "True Positive"))
        __sortingEnabled = self.truePositiveTable.isSortingEnabled()
        self.truePositiveTable.setSortingEnabled(False)
        item = self.truePositiveTable.item(0, 0)
        item.setText(_translate("TruePositiveWindow", "User Sign"))
        item = self.truePositiveTable.item(0, 1)
        item.setText(_translate("TruePositiveWindow", "TSP/GT"))
        item = self.truePositiveTable.item(0, 2)
        item.setText(_translate("TruePositiveWindow", "IOU"))
        item = self.truePositiveTable.item(0, 3)
        item.setText(_translate("TruePositiveWindow", "NSP Count"))
        item = self.truePositiveTable.item(0, 4)
        item.setText(_translate("TruePositiveWindow", "Score"))
        self.truePositiveTable.setSortingEnabled(__sortingEnabled)
    def resetRow(self, count):
        self.truePositiveTable.setRowCount(count)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TruePositiveWindow = QtWidgets.QMainWindow()
    ui = Ui_TruePositiveWindow()
    ui.setupUi(TruePositiveWindow)
    TruePositiveWindow.show()
    sys.exit(app.exec_())
