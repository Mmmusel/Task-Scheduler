import pickle

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import global_user
import mainWindow
import 注册
from graphHTML import goto_creat_icon_html


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.Mainwindow = MainWindow
        self.Mainwindow.setStyleSheet("background-color:rgb(234,195,154)")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 400)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(40, 200, 320, 30)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(40, 250, 320, 30)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(40, 300, 150, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(210, 300, 150, 30)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 296, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda:self.usr_sign_up())
        self.pushButton_2.clicked.connect(lambda:self.usr_login())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setPlaceholderText("请输入用户名")
        self.lineEdit.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_2.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.pushButton.setStyleSheet("#pushButton{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_2:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_2:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.icon = QWebEngineView(MainWindow)
        the_html_content = goto_creat_icon_html()
        self.icon.setHtml(the_html_content)
        self.icon.setGeometry(130, 50, 150, 150)
        self.icon.show()

        MainWindow.setStyleSheet('background-color:rgb(255,255,255)')
        self.close_button = QtWidgets.QPushButton(MainWindow)
        self.close_button.setGeometry(370, 0, 30, 30)
        icon = QIcon(QPixmap('退出键.png').scaled(QSize(50, 50)))
        self.close_button.setIcon(icon)
        self.close_button.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))

    def usr_sign_up(self):
        window_sign_up = QMainWindow()
        sign_up_ui = 注册.Ui_MainWindow()
        sign_up_ui.setupUi(window_sign_up)
        window_sign_up.show()

    def usr_login(self):
        # 拿账号
        usr_name = self.lineEdit.text()
        # 拿密码
        usr_pwd = self.lineEdit_2.text()
        # 设置管理员
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        # 如果用户名正确
        if usr_name in usrs_info:
            # 如果密码正确
            if usr_pwd == usrs_info[usr_name]:
                global_user.setName(usr_name)
                # 弹窗信息
                #messagebox.showinfo(title='Welcome', message=usr_name + ' 登陆成功!')
                QMessageBox.information(self.Mainwindow,"Welcome", usr_name + ' 登录成功!')
                self.Mainwindow.close()
                #app = QApplication(sys.argv)
                MainWindow = mainWindow.Ui_MainWindow()
                MainWindow.update()
                MainWindow.show()
                #sys.exit(app.exec_())
            else:
                # 弹窗错误
                QMessageBox.critical(self.Mainwindow, "error", '密码错误!')
                #messagebox.showerror(message='Wrong password!')
        else:
            # 提示窗口
            #is_sign_up = messagebox.askyesno(message=usr_name + ' has not registered, whether to register?')
            is_sign_up = QMessageBox.question(self.Mainwindow, 'not register', usr_name + ' 还没有注册，是否立即注册?', QMessageBox.Yes, QMessageBox.No)
            if is_sign_up == QMessageBox.Yes:
                self.usr_sign_up()
