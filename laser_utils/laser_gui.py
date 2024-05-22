# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laser_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 427)
        MainWindow.setStyleSheet("background-color:rgb(219, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 431, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.StopfireButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.StopfireButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.StopfireButton.setObjectName("StopfireButton")
        self.gridLayout.addWidget(self.StopfireButton, 2, 1, 1, 1)
        self.ArmButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ArmButton.setStyleSheet("background-color: rgb(255, 227, 16);")
        self.ArmButton.setObjectName("ArmButton")
        self.gridLayout.addWidget(self.ArmButton, 1, 0, 1, 1)
        self.DisarmButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DisarmButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.DisarmButton.setObjectName("DisarmButton")
        self.gridLayout.addWidget(self.DisarmButton, 1, 1, 1, 1)
        self.FireButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FireButton.setStyleSheet("background-color: rgb(81, 255, 51);")
        self.FireButton.setObjectName("FireButton")
        self.gridLayout.addWidget(self.FireButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 341, 21))
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.Clock.setGeometry(QtCore.QRect(30, 140, 211, 61))
        self.Clock.setObjectName("Clock")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 341, 21))
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(530, 40, 341, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ConnectOphir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ConnectOphir.setObjectName("ConnectOphir")
        self.gridLayout_2.addWidget(self.ConnectOphir, 0, 0, 1, 1)
        self.ArmOphir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ArmOphir.setObjectName("ArmOphir")
        self.gridLayout_2.addWidget(self.ArmOphir, 1, 0, 1, 1)
        self.StatusOphir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.StatusOphir.setObjectName("StatusOphir")
        self.gridLayout_2.addWidget(self.StatusOphir, 0, 1, 1, 1)
        self.DisarmOphir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.DisarmOphir.setObjectName("DisarmOphir")
        self.gridLayout_2.addWidget(self.DisarmOphir, 1, 1, 1, 1)
        self.Console = QtWidgets.QTextEdit(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(30, 220, 841, 181))
        self.Console.setStyleSheet("background: rgb(255, 255, 255)")
        self.Console.setObjectName("Console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StopfireButton.setText(_translate("MainWindow", "STOP FIRE"))
        self.ArmButton.setText(_translate("MainWindow", "ARM"))
        self.DisarmButton.setText(_translate("MainWindow", "DISARM"))
        self.FireButton.setText(_translate("MainWindow", "FIRE"))
        self.label.setText(_translate("MainWindow", "LAMP LASER 100 Hz  "))
        self.label_2.setText(_translate("MainWindow", "OPHIR"))
        self.ConnectOphir.setText(_translate("MainWindow", "CONNECT"))
        self.ArmOphir.setText(_translate("MainWindow", "ARM OPHIR"))
        self.StatusOphir.setText(_translate("MainWindow", "STATUS"))
        self.DisarmOphir.setText(_translate("MainWindow", "DISARM OPHIR"))
