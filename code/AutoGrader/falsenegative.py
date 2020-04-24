# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'falsenegative.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FalseNegativeWindow(object):
    def setupUi(self, FalseNegativeWindow):
        FalseNegativeWindow.setObjectName("FalseNegativeWindow")
        FalseNegativeWindow.resize(808, 611)
        self.centralwidget = QtWidgets.QWidget(FalseNegativeWindow)
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
        self.FalseNegativeLabel = QtWidgets.QLabel(self.centralwidget)
        self.FalseNegativeLabel.setGeometry(QtCore.QRect(350, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.FalseNegativeLabel.setFont(font)
        self.FalseNegativeLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.FalseNegativeLabel.setObjectName("FalseNegativeLabel")
        self.falseNegativeTable = QtWidgets.QTableWidget(self.centralwidget)
        self.falseNegativeTable.setGeometry(QtCore.QRect(310, 210, 241, 281))
        self.falseNegativeTable.setRowCount(12)
        self.falseNegativeTable.setColumnCount(2)
        self.falseNegativeTable.setObjectName("falseNegativeTable")
        item = QtWidgets.QTableWidgetItem()
        self.falseNegativeTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.falseNegativeTable.setItem(0, 1, item)
        FalseNegativeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FalseNegativeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        FalseNegativeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FalseNegativeWindow)
        self.statusbar.setObjectName("statusbar")
        FalseNegativeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FalseNegativeWindow)
        QtCore.QMetaObject.connectSlotsByName(FalseNegativeWindow)

    def retranslateUi(self, FalseNegativeWindow):
        _translate = QtCore.QCoreApplication.translate
        FalseNegativeWindow.setWindowTitle(_translate("FalseNegativeWindow", "MainWindow"))
        self.titleLabel.setText(_translate("FalseNegativeWindow", "3D Point Cloud Autograder"))
        self.FalseNegativeLabel.setText(_translate("FalseNegativeWindow", "False Negative"))
        __sortingEnabled = self.falseNegativeTable.isSortingEnabled()
        self.falseNegativeTable.setSortingEnabled(False)
        item = self.falseNegativeTable.item(0, 0)
        item.setText(_translate("FalseNegativeWindow", "Sign"))
        item = self.falseNegativeTable.item(0, 1)
        item.setText(_translate("FalseNegativeWindow", "# of Points"))
        self.falseNegativeTable.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FalseNegativeWindow = QtWidgets.QMainWindow()
    ui = Ui_FalseNegativeWindow()
    ui.setupUi(FalseNegativeWindow)
    FalseNegativeWindow.show()
    sys.exit(app.exec_())
