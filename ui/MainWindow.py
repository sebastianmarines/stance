# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1206, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.counter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.counter.setFont(font)
        self.counter.setAlignment(QtCore.Qt.AlignCenter)
        self.counter.setObjectName("counter")
        self.gridLayout.addWidget(self.counter, 3, 1, 1, 1)
        self.instructions = QtWidgets.QLabel(self.centralwidget)
        self.instructions.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.instructions.setFont(font)
        self.instructions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instructions.setScaledContents(True)
        self.instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.instructions.setObjectName("instructions")
        self.gridLayout.addWidget(self.instructions, 0, 1, 1, 1)
        self.current_image = QtWidgets.QLabel(self.centralwidget)
        self.current_image.setMaximumSize(QtCore.QSize(350, 240))
        self.current_image.setText("")
        self.current_image.setScaledContents(True)
        self.current_image.setObjectName("current_image")
        self.gridLayout.addWidget(self.current_image, 2, 1, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 3, 0, 1, 1)
        self.webcam = QtWidgets.QLabel(self.centralwidget)
        self.webcam.setEnabled(True)
        self.webcam.setMaximumSize(QtCore.QSize(640, 480))
        self.webcam.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.webcam.setText("")
        self.webcam.setScaledContents(True)
        self.webcam.setObjectName("webcam")
        self.gridLayout.addWidget(self.webcam, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pose = QtWidgets.QLabel(self.centralwidget)
        self.pose.setMaximumSize(QtCore.QSize(16777215, 10))
        self.pose.setText("")
        self.pose.setAlignment(QtCore.Qt.AlignCenter)
        self.pose.setObjectName("pose")
        self.gridLayout.addWidget(self.pose, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.counter.setText(_translate("MainWindow", "5"))
        self.instructions.setText(_translate("MainWindow", "Presiona el boton de iniciar para comenzar"))
        self.start.setText(_translate("MainWindow", "Iniciar"))
        self.label.setText(_translate("MainWindow",
                                      "Antes de iniciar asegurate de que la computadora detecte tu cara y veas puntos rojos sobre ella"))
