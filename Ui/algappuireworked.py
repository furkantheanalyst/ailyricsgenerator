# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'algappreworked.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(644, 866)
        MainWindow.setMinimumSize(QtCore.QSize(644, 866))
        MainWindow.setMaximumSize(QtCore.QSize(644, 866))
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(240, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.lbl_seed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_seed.setGeometry(QtCore.QRect(10, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_seed.setFont(font)
        self.lbl_seed.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.lbl_seed.setObjectName("lbl_seed")
        self.lbl_length = QtWidgets.QLabel(self.centralwidget)
        self.lbl_length.setGeometry(QtCore.QRect(10, 140, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_length.setFont(font)
        self.lbl_length.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.lbl_length.setObjectName("lbl_length")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(430, 180, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("color: rgb(0, 0, 0);")
        self.btn_start.setObjectName("btn_start")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(570, 180, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.btn_clear.setObjectName("btn_clear")
        self.lbl_song = QtWidgets.QLabel(self.centralwidget)
        self.lbl_song.setEnabled(True)
        self.lbl_song.setGeometry(QtCore.QRect(0, 220, 651, 651))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_song.setFont(font)
        self.lbl_song.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lbl_song.setText("")
        self.lbl_song.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_song.setObjectName("lbl_song")
        self.lbl_song.setWordWrap(1)
        self.tbx_seed = QtWidgets.QLineEdit(self.centralwidget)
        self.tbx_seed.setGeometry(QtCore.QRect(440, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbx_seed.setFont(font)
        self.tbx_seed.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.tbx_seed.setObjectName("tbx_seed")
        self.tbx_length = QtWidgets.QLineEdit(self.centralwidget)
        self.tbx_length.setGeometry(QtCore.QRect(440, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbx_length.setFont(font)
        self.tbx_length.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.tbx_length.setObjectName("tbx_length")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ALGAPP ver 1.0"))
        self.label.setText(_translate("MainWindow", "ALGAPP"))
        self.lbl_seed.setText(_translate("MainWindow", "Input a seed for song"))
        self.lbl_length.setText(_translate("MainWindow", "How many words do you want?"))
        self.btn_start.setText(_translate("MainWindow", "Create a Song"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.tbx_seed.setText(_translate("MainWindow", "I'm good enough"))
        self.tbx_length.setText(_translate("MainWindow", "60"))

