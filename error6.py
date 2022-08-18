# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog


class Ui_Dialoge6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 220)
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet("#centralWidget{background:rgba(0,255,255,0.4);}"
                             "#label{background:rgba(255,255,0,1);}"
                             "#widget{background:rgba(0,255,255,1);}")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 70, 340, 80))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("    color: rgb(0, 0, 0);\n"
                                       "    background-color: rgb(255,255,255);\n"
                                       "    border: 3px solid rgb(3, 3, 3);\n"
                                       "    border-radius:10px;\n"
                                       "    font: 25 9pt \"Microsoft YaHei\";")

        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(380, 70, 30, 30)
        #采用的相对位置  要是修改textBrowser时  记得修改这里  第一二个参数  第一个参数 = testBrowser的para1 + para3 - 30 第二个参数 = para2
        icon = QIcon(QPixmap('退出键.png').scaled(QSize(50, 50)))
        self.close_button.setIcon(icon)
        self.close_button.clicked.connect(Dialog.close)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Microsoft YaHei\'; font-size:9pt; font-weight:24; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">"
                                            "tags标签已达上限 </span></p></body></html>"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Dialoge()
    win = QDialog()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())