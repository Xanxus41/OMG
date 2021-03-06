# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random, Tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPixmap


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        n = random.random()
        path = Tools.IMG_PATH1
        r = 193;g = 255;b = 193
        if (n < 0.2):
            path = Tools.IMG_PATH2
            r = 150;g = 0;b = 0
        elif(n<0.4):
            path = Tools.IMG_PATH3
            r = 153;g = 50;b = 204
        elif(n<0.6):
            path = Tools.IMG_PATH4
            r = 70;g = 130;b = 180
        elif(n<0.8):
            path = Tools.IMG_PATH5
            r = 25;g = 25;b = 112

        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(865, 605)
        MainWidget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWidget.setMinimumSize(865, 605)
        MainWidget.setMaximumSize(865, 605)
        palette = QtGui.QPalette()
        palette.setColor(MainWidget.backgroundRole(), QColor(r, g, b))  # 背景颜色
        MainWidget.setPalette(palette)
        MainWidget.setAutoFillBackground(True)

        self.SkillTableView = QtWidgets.QTableView(MainWidget)
        self.SkillTableView.setGeometry(QtCore.QRect(170, 30, 513, 561))
        self.SkillTableView.setObjectName("SkillTableView")

        self.ComboTableView = QtWidgets.QTableView(MainWidget)
        self.ComboTableView.setGeometry(QtCore.QRect(700, 30, 150, 561))
        self.ComboTableView.setObjectName("ComboTableView")

        self.startBtn = QtWidgets.QPushButton(MainWidget)
        self.startBtn.setGeometry(QtCore.QRect(15, 30, 140, 61))
        self.startBtn.setObjectName("startBtn")

        self.start2Btn = QtWidgets.QPushButton(MainWidget)
        self.start2Btn.setGeometry(QtCore.QRect(15, 100, 140, 61))
        self.start2Btn.setObjectName("startBtn2")

        self.updateBtn = QtWidgets.QPushButton(MainWidget)
        self.updateBtn.setGeometry(QtCore.QRect(15, 170, 140, 61))
        self.updateBtn.setObjectName("updateBtn")

        self.messageLaber = QtWidgets.QLabel(MainWidget)
        self.messageLaber.setGeometry(QtCore.QRect(5, 95, 400, 20))

        self.laber = QtWidgets.QLabel(MainWidget)
        self.laber.setGeometry(QtCore.QRect(5, 5, 400, 20))
        self.laber.setText('单屏启动后5秒内切到dota2选择技能界面，等待5秒')

        self.imgLaber = QtWidgets.QLabel(MainWidget)
        self.imgLaber.setGeometry(QtCore.QRect(0, 270, 170, 340))

        self.imgLaber.setPixmap(QPixmap(path))
        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "OMG"))
        self.startBtn.setText(_translate("MainWidget", "单屏启动"))
        self.start2Btn.setText(_translate("MainWidget", "双屏启动"))
        self.updateBtn.setText(_translate("MainWidget", "更新数据"))
