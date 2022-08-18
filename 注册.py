import os
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 260)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.Mainwindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        '''
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(40,40,90,30)
        self.label.setObjectName("label")
        self.label.setFont(font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(40, 90, 90, 30)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(40,140,200,30)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        '''
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 320, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 90, 320, 30))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 140,320, 30))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(QtCore.QRect(95, 200, 200, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 298, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda:self.sign_to_Mofan_Python())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setPlaceholderText("请输入用户名")
        self.lineEdit.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_2.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.lineEdit_3.setPlaceholderText("请确认密码")
        self.lineEdit_3.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.pushButton.setStyleSheet('	color: rgb(0, 0, 0);border: 3px solid rgb(0,0,0);border-radius:10px;')
        self.close_button = QtWidgets.QPushButton(MainWindow)
        self.close_button.setGeometry(370, 0, 30, 30)
        icon = QIcon(QPixmap('退出键.png').scaled(QSize(50, 50)))
        self.close_button.setIcon(icon)
        self.close_button.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "Account"))
        #self.label_2.setText(_translate("MainWindow", "Password"))
        #self.label_3.setText(_translate("MainWindow", "Password confirm"))
        self.pushButton.setText(_translate("MainWindow", "立即注册"))

    def sign_to_Mofan_Python(self):
        np = self.lineEdit.text()  # 密码
        npf = self.lineEdit_2.text()  # 确认密码
        nn = self.lineEdit_3.text()  # 用户名
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            print(exist_usr_info)
        # 如果两次密码不一致
        if np != npf:
            #messagebox.showerror(message='Two passwords are inconsistent!')
            QMessageBox.critical(self.Mainwindow, "error", "两次密码输入不一致!")
        # 否则如果用户名存在
        elif nn in exist_usr_info:
            #messagebox.showerror(message=nn + ' already exists, please choose another account name!')
            QMessageBox.critical(self.Mainwindow, "error", nn + ' 已经存在，请选择其他用户名')
        else:
            # 保存输入的账号密码
            exist_usr_info[str(nn)] = str(np)
            with open('usrs_info.pickle', 'wb') as usr_file:
                # 存数据
                pickle.dump(exist_usr_info, usr_file)
                print(exist_usr_info)
                #messagebox.showinfo(message='Successfully registered!')
                QMessageBox.information(self.Mainwindow, "registered",
                                     '注册成功!')
            os.mkdir('data\\' + nn)
            f = open('data\\' + nn + '\\' + "routine.txt", 'w')
            f.close()
            f = open('data\\' + nn + '\\' + "tags.txt", 'w')
            f.write('study\nsport')
            f.close()
            f = open('data\\' + nn + '\\' + "ToDo.txt", 'w')
            f.close()
        # 销毁窗口
            self.Mainwindow.close()
