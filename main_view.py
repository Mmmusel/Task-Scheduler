from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from calendar import weekday
from datetime import datetime, timedelta
n = datetime.now()

weekPath = []
dateleft = 1 - int(n.strftime('%w'))
if dateleft == 1:
    dateleft = -6
for i in range(0, 7):
    ddd = i+dateleft
    dayStr = (n + timedelta(days=ddd)).strftime('%Y/%m/%d')
    weekPath.append(dayStr)


class Ui_MainWindowxx(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton()
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(200, 30)
        #self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_4:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_4:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(200, 30)
        #self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";\n"
                                "border-radius: 4px;\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(198, 198, 198);")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(200, 30)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_3:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_3:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        #self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(200, 30)
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
        #self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                    "border-radius: 4px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(198, 198, 198);")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton()
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setMinimumSize(100, 30)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_5:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_5:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)

        ######
        self.pushButton_7 = QtWidgets.QPushButton()
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setMinimumSize(100, 30)
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_7:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_7:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 2, 1)

        self.pushButton_8 = QtWidgets.QPushButton()
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setMinimumSize(100, 30)
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_8:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_8:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 2, 1)
        ####

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("#listWidget::item {\n"
                                    "    background-color: #ffffff;\n"
                                    "    color: #000000;\n"
                                    "    border: transparent;\n"
                                    "    border-bottom: 1px solid #dbdbdb;\n"
                                    "    padding: 8px;\n"
                                    "}\n"
                                    "\n"
                                    "#listWidget::item:hover {\n"
                                    "    background-color: #f5f5f5;\n"
                                    "}\n"
                                    "\n"
                                    "#listWidget::item:selected {\n"
                                    "    border-left: 5px solid #777777;\n"
                                    "}\n"
                                    "QListView {\n"
                                    "    font: 25 9pt \"Microsoft YaHei\";\n"
                                    "    border: 15px solid white; /* 设置边框的大小，样式，颜色 */\n"
                                    "    border-radius: 10px;\n"
                                    "}")
        self.gridLayout.addWidget(self.listWidget, 5, 0, 1, 2)
        self.listWidget_2 = QtWidgets.QListWidget()
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet("#listWidget::item {\n"
                                        "    background-color: #ffffff;\n"
                                        "    color: #000000;\n"
                                        "    border: transparent;\n"
                                        "    border-bottom: 1px solid #dbdbdb;\n"
                                        "    padding: 8px;\n"
                                        "}\n"
                                        "\n"
                                        "#listWidget::item:hover {\n"
                                        "    background-color: #f5f5f5;\n"
                                        "}\n"
                                        "\n"
                                        "#listWidget::item:selected {\n"
                                        "    border-left: 5px solid #777777;\n"
                                        "}\n"
                                        "QListView {\n"
                                        "    font: 25 9pt \"Microsoft YaHei\";\n"
                                        "    border: 15px solid white; /* 设置边框的大小，样式，颜色 */\n"
                                        "    border-radius: 10px;\n"
                                        "}")
        self.gridLayout.addWidget(self.listWidget_2, 7, 0, 1, 2)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止通过表格编辑
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setStyleSheet("QHeaderView\n"
                                        "{\n"
                                        "    background:transparent;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section\n"
                                        "{\n"
                                        "    font-size:14px;\n"
                                        "    font-family:\"Microsoft YaHei\";\n"
                                        "    color:#FFFFFF;\n"
                                        "    background:rgb(113, 113, 113);\n"
                                        "    border:none;\n"
                                        "    text-align:left;\n"
                                        "    min-height:49px;\n"
                                        "    max-height:49px;\n"
                                        "    margin-left:0px;\n"
                                        "    padding-left:0px;\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget\n"
                                        "{\n"
                                        "    background:#FFFFFF;\n"
                                        "    border:none;\n"
                                        "\n"
                                        "    font-size:20px;\n"
                                        "    font-family:\"Microsoft YaHei\";\n"
                                        "    color:#666666;\n"
                                        "    font: 25 9pt \"Microsoft YaHei\";\n"
                                        "    border: 15px solid white; /* 设置边框的大小，样式，颜色 */\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QTableWidget::item\n"
                                        "{\n"
                                        "    border-bottom:1px solid #EEF1F7 ;\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget::item::selected\n"
                                        "{\n"
                                        "    color:red;\n"
                                        "    background:#EFF4FF;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QScrollBar::handle:vertical\n"
                                        "{\n"
                                        "    background: rgba(255,255,255,20%);\n"
                                        "    border: 0px solid grey;\n"
                                        "    border-radius:3px;\n"
                                        "    width: 8px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                        "{\n"
                                        "    background:rgba(255,255,255,10%);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QScollBar::add-line:vertical, QScrollBar::sub-line:vertical\n"
                                        "{\n"
                                        "    background:transparent;\n"
                                        "}\n"
                                        "")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 2, 8, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1578, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "新建固定事项"))
        self.pushButton_4.setText(_translate("MainWindow", "新建日常任务"))
        self.label.setText(_translate("MainWindow", "Click Table:"))
        self.pushButton_3.setText(_translate("MainWindow", "新建事项分类"))
        self.pushButton_2.setText(_translate("MainWindow", "新建待办事项"))
        self.label_3.setText(_translate("MainWindow", "ToDo:"))
        self.pushButton_5.setText(_translate("MainWindow", "一键安排"))
        self.pushButton_7.setText(_translate("MainWindow", "\n上周\n"))
        self.pushButton_8.setText(_translate("MainWindow", "\n下周\n"))

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "00:00-01:59"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "02:00-03:59"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "04:00-05:59"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "06:00-07:59"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "08:00-09:59"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "10:00-11:59"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "12:00-13:59"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "14:00-15:59"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "16:00-17:59"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "18:00-19:59"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "20:00-21:59"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "22:00-23:59"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MON"+'\n'+weekPath[0]))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TUE"+'\n'+weekPath[1]))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "WED"+'\n'+weekPath[2]))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TUR"+'\n'+weekPath[3]))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "FRI"+'\n'+weekPath[4]))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SAT"+'\n'+weekPath[5]))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SUN"+'\n'+weekPath[6]))
