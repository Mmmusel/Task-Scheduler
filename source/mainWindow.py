import calendar
import time
import maind
import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QBrush, QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTabWidget, QHBoxLayout, QLabel, QCheckBox, \
    QGridLayout, QFileDialog, QToolButton, QApplication, QWidget, QPushButton
from graphHTML import goto_creat_empty_html, goto_creat_daypie_html, goto_creat_week_pie_line_html, \
    goto_creat_month_bar_html
from timeTools import cal_minute_duration, cal_date_to_week, cal_date_to_month

from var import desk_path
import global_user


class Ui_MainWindow(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置透明和tabbar高度
        self.dailyTxt=[]
        self.setStyleSheet("QTabBar:tab{height:60}QTabWidget:pane {border-top:0px solid #e8f3f9;background: transparent; }")
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, 'tab 1')
        self.addTab(self.tab2, 'tab 2')
        self.addTab(self.tab3, 'tab 3')
        self.setTabIcon(0, QIcon(QPixmap('周.png').scaled(60,60)))
        self.setTabToolTip(0, '周视图')
        self.setTabToolTip(1, '月视图')
        self.setTabToolTip(2, '日视图')
        self.setTabIcon(1, QIcon(QPixmap('日历.png').scaled(60,60)))
        self.setTabIcon(2,QIcon(QPixmap('日视图.png').scaled(60,60)))
        self.color = ['102, 255, 255', '160,82,45', '255,192,203']  # TODO
        self.colorflag = 0
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()
        self.currentChanged.connect(self.changed)  ####   切换页面的刷新！！！ 定义一个刷新函数
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setMinimumSize(1400, 700)
        self.initColor()
        self.changeColor()
    # 页面1
    def tab1_ui(self):
        self.setTabText(0, '')
        self.lay1 = QGridLayout()
        self.lay1.addWidget(maind.window, 0, 0, 1, 1)
        self.tagsInit()
        maind.window.initRoutine()
        maind.window.initTable()
        maind.window.initToDo()

        btn7 = maind.window.main_view.pushButton_7
        btn7.clicked.connect((lambda:maind.window.change1()))

        btn8 = maind.window.main_view.pushButton_8
        btn8.clicked.connect((lambda:maind.window.change2()))
        self.tab1.setLayout(self.lay1)

    def tagsInit(self):
        f = open(desk_path + global_user.getName() + '/' + "tags.txt", "r")
        ddd=f.read().split('\n')
        maind.child.in_dialog.comboBox.addItems(ddd)
        maind.child2.free_create.comboBox.addItems(ddd)
        maind.child4.routine.comboBox.addItems(ddd)
        maind.child1_edit.edit1.comboBox.addItems(ddd)
        maind.child2_edit.edit3.comboBox.addItems(ddd)
        maind.child4_edit.edit4.comboBox.addItems(ddd)
        f.close()

    # 页面2
    def tab2_ui(self):
        self.setTabText(1, '')
        ##################################################
        t = time.localtime()
        self.Year = t.tm_year
        self.Month = t.tm_mon
        self.Day = t.tm_mday

        #self.label_13 = QtWidgets.QLabel(self.tab2)  # 显示选中日期：
        #self.label_13.setText(str(self.Year) + ' /' + str(self.Month) + ' /' + str(self.Day))

        self.layout_calendar = QGridLayout()  # 日历

        # 日历第一排
        blue = QtWidgets.QWidget()
        layout_blue = QGridLayout()

        self.label_1 = QtWidgets.QLabel(self.tab2)  # 日历头蓝底
        self.label_1.setStyleSheet("background:rgba(113, 113, 113,105)")
        layout_blue.addWidget(self.label_1, 0, 0, 1, 8)
        self.pushButton_1 = QPushButton(self.tab2)  # 年份递减按钮
        self.pushButton_1.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue.addWidget(self.pushButton_1, 0, 0)
        self.pushButton_2 = QPushButton(self.tab2)  # 月份递减按钮
        self.pushButton_2.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue.addWidget(self.pushButton_2, 0, 1)
        self.pushButton_3 = QPushButton(self.tab2)  # 月份递增按钮
        self.pushButton_3.setStyleSheet("background:rgba(113, 113, 113,55)")
        layout_blue.addWidget(self.pushButton_3, 0, 6)
        self.pushButton_4 = QPushButton(self.tab2)  # 年份递增按钮
        self.pushButton_4.setStyleSheet("background:rgba(113, 113, 113,55)")
        layout_blue.addWidget(self.pushButton_4, 0, 7)
        self.label_2 = QtWidgets.QLabel(self.tab2)  # 年份
        self.label_2.setStyleSheet("background:rgba(113, 113, 113, 55)")
        self.label_2.setAlignment(Qt.AlignCenter)
        layout_blue.addWidget(self.label_2, 0, 3)
        self.label_3 = QtWidgets.QLabel(self.tab2)  # 月份
        self.label_3.setStyleSheet("background:rgba(113, 113, 113, 55)")
        self.label_3.setAlignment(Qt.AlignCenter)
        layout_blue.addWidget(self.label_3, 0, 4)

        self.label_1.raise_()  # 蓝底
        self.pushButton_1.raise_()  # 年份递减
        self.pushButton_2.raise_()  # 月份递减
        self.pushButton_3.raise_()  # 月份递增
        self.pushButton_4.raise_()  # 年份递增
        self.label_2.raise_()  # 年份
        self.label_3.raise_()  # 月份

        blue.setLayout(layout_blue)
        self.layout_calendar.addWidget(blue, 0, 0)
        self.layout_calendar.setRowStretch(0, 1)

        # 日历第二排
        white = QtWidgets.QWidget()
        layout_white = QGridLayout()
        self.label_11 = QtWidgets.QLabel(self.tab2)  # 白底
        self.label_11.setStyleSheet("background:rgba(255, 255, 255, 255)")
        self.label_11.setText("")
        layout_white.addWidget(self.label_11, 0, 0, 1, 7)
        self.label_4 = QtWidgets.QLabel(self.tab2)  # 周一
        self.label_4.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_4.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_4, 0, 0)
        self.label_5 = QtWidgets.QLabel(self.tab2)  # 周二
        self.label_5.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_5.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_5, 0, 1)
        self.label_6 = QtWidgets.QLabel(self.tab2)  # 周三
        self.label_6.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_6.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_6, 0, 2)
        self.label_7 = QtWidgets.QLabel(self.tab2)  # 周四
        self.label_7.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_7.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_7, 0, 3)
        self.label_8 = QtWidgets.QLabel(self.tab2)  # 周五
        self.label_8.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_8.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_8, 0, 4)
        self.label_9 = QtWidgets.QLabel(self.tab2)  # 周六
        self.label_9.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_9.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_9, 0, 5)
        self.label_10 = QtWidgets.QLabel(self.tab2)  # 周日
        self.label_10.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_10.setAlignment(Qt.AlignCenter)
        layout_white.addWidget(self.label_10, 0, 6)
        self.label_11 = QtWidgets.QLabel(self.tab2)  # 白底
        self.label_11.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")

        self.label_11.raise_()  # 白底
        self.label_4.raise_()  # 周一
        self.label_5.raise_()  # 周二
        self.label_6.raise_()  # 周三
        self.label_7.raise_()  # 周四
        self.label_8.raise_()  # 周五
        self.label_9.raise_()  # 周六
        self.label_10.raise_()  # 周日

        white.setLayout(layout_white)
        self.layout_calendar.addWidget(white, 1, 0)
        self.layout_calendar.setRowStretch(1, 1)
        ##################################################

        ##################################################
        # 一些显示和设置
        self.initCalender()  # 显示周一到周日以及<<、<、>、>>

        self.date = []  # 31个日期按钮
        _translate = QtCore.QCoreApplication.translate
        for i in range(31):
            tmp = QPushButton(self.tab2)
            tmp.setText(_translate("MainWindow", str(i + 1)))
            self.date.append(tmp)

        self.setPushButton()  # 设置年份月份加减键、31个日期键对应的函数
        self.getImportance()  # 获取重要性
        self.printCalender()  # 打印日历
        ##################################################

        ##################
        #个性化设置区

        self.setting = QtWidgets.QWidget(self)
        self.setting.resize(300, 45)
        # 背景按钮
        self.pushButton_5 = QToolButton(self.setting)
        self.pushButton_5.setFixedSize(40, 40)
        self.pushButton_5.setText(_translate("MainWindow", ""))
        icon = QIcon('背景图标.png')
        self.pushButton_5.setToolTip("更换背景")
        self.pushButton_5.setIconSize(QtCore.QSize(self.pushButton_5.width(), self.pushButton_5.height()))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.clicked.connect(lambda: self.setBackground())

        # 头像按钮
        self.flag = 0
        self.pushButton_8 = QToolButton(self.setting)
        self.pushButton_8.setText(_translate("MainWindow", ""))
        self.pushButton_8.setFixedSize(40,40)
        self.pushButton_8.setToolTip("更换头像")
        f = open('用户头像信息.txt')
        lines = f.readlines()
        icon = QIcon(QPixmap('初始头像.png').scaled(self.pushButton_8.rect().size()))
        for line in lines:
            if line.split()[0].__eq__(global_user.getName()):
                icon = QIcon(QPixmap((line.split(' ', 1)[1]).replace('\n', '')).scaled(self.pushButton_8.rect().size()))
        f.close()
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(self.pushButton_8.width(), self.pushButton_8.height()))
        self.pushButton_8.clicked.connect(lambda: self.changeProfile())

        self.setCornerWidget(self.setting,corner=Qt.TopRightCorner)

        self.close_button = QtWidgets.QToolButton(self.setting)
        self.close_button.setFixedSize(40, 40)
        self.close_button.setToolTip("退出")
        icon = QIcon(QPixmap('退出键.png').scaled(QSize(40, 40)))
        self.close_button.setIcon(icon)
        self.close_button.clicked.connect(self.close)

        self.max_button = QtWidgets.QToolButton(self.setting)
        self.max_button.setToolTip("全屏显示")
        self.max_button.setFixedSize(40, 40)
        icon = QIcon(QPixmap('全屏.png').scaled(QSize(40, 40)))
        self.max_button.setIcon(icon)
        self.max_button.clicked.connect(lambda:self.resizeWindow())

        # 更换主题颜色按钮
        self.pushButton_10 = QToolButton(self.setting)
        self.pushButton_10.setFixedSize(40, 40)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText(_translate("MainWindow", ""))
        self.pushButton_10.setToolTip("更换主题色")
        self.pushButton_10.setStyleSheet('#pushButton_10 {border-radius:20px;background-color:rgba(102, 255, 255, 255); }')
        self.pushButton_10.clicked.connect(lambda: self.changeColor()) # TODO

        pHLayout = QHBoxLayout(self.setting)
        pHLayout.addWidget(self.pushButton_5)
        pHLayout.addWidget(self.pushButton_8)
        pHLayout.addWidget(self.max_button)
        pHLayout.addWidget(self.pushButton_10)
        pHLayout.addWidget(self.close_button)
        ##################

        ##################################################
        # 日历按钮区
        button = QtWidgets.QWidget()

        layout_button = QGridLayout()

        font = QtGui.QFont()
        font.setPointSize(13)
        # 提示语
        self.label_12 = QLabel(self.tab2)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setText("当前没有日期被选中")
        layout_button.addWidget(self.label_12, 1, 0, 1, 2)
        #layout_button.addWidget(self.label_13, 1, 0, 1, 2)

        # 分析当前日期所在月份的数据按钮
        self.pushButton_6 = QPushButton(self.tab2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setFixedSize(400,50)
        self.pushButton_6.setText(_translate("MainWindow", "展示当前选择月份的数据分析"))
        self.pushButton_6.clicked.connect(lambda: self.analyze_month())
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_6:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_6:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")
        layout_button.addWidget(self.pushButton_6, 2, 0, 1, 1)

        # 分析当前日期所在周的数据按钮
        self.pushButton_7 = QPushButton(self.tab2)
        self.pushButton_7.setFixedSize(400, 50)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText(_translate("MainWindow", "展示当前选择星期的数据分析"))
        self.pushButton_7.clicked.connect(lambda: self.analyze_week())
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
        self.choosed_a_date = 0  # 当前还未选择一个日期
        layout_button.addWidget(self.pushButton_7, 2, 1, 1, 1)

        button.setLayout(layout_button)
        self.layout_calendar.addWidget(button, 3, 0)
        self.layout_calendar.setRowStretch(3, 3)
        ##################################################

        ##################################################
        # 添加日历布局
        cal = QtWidgets.QWidget()
        cal.setLayout(self.layout_calendar)
        self.top = QGridLayout()
        self.top.addWidget(cal, 0, 0)

        # 添加html布局
        self.empty_html("请点击左侧日历选择一个日期")
        self.tab2.setLayout(self.top)
        ##################################################

    def uploadDay(self):
        self.myFilter()
        self.listWidget33.clear()

        show = []
        if len(self.dailyTxt):
            for k in self.dailyTxt:
                s = k.split(';')
                if s[5] not in self.IMPfilter:
                    continue
                if s[6] not in self.TAGfilter:
                    continue
                if s[8] not in self.STATEfilter:
                    continue
                #if s[1] == '':
                #    s[2] = s[4]
                show.append(s)
            show.sort(key=lambda x: (x[2]))
            for s in show:
                self.listWidget33.addItem(s[0] + ' ' + s[2])

    def tab3_ui(self):
        self.setTabText(2, '')

        ##################################################

        self.tag = QtWidgets.QWidget()
        layout_tag3 = QGridLayout()
        self.tag1 = QLabel('重要性: ')
        layout_tag3.addWidget(self.tag1, 0, 0)
        self.tag1_1 = QCheckBox('1')
        layout_tag3.addWidget(self.tag1_1, 0, 1)
        self.tag1_2 = QCheckBox('2')
        layout_tag3.addWidget(self.tag1_2, 0, 2)
        self.tag1_3 = QCheckBox('3')
        layout_tag3.addWidget(self.tag1_3, 0, 3)
        self.tag1_4 = QCheckBox('4')
        layout_tag3.addWidget(self.tag1_4, 0, 4)
        self.tag1_5 = QCheckBox('5')
        layout_tag3.addWidget(self.tag1_5, 0, 5)

        self.tag2 = QLabel('状态: ')
        layout_tag3.addWidget(self.tag2, 1, 0)
        self.tag2_1 = QCheckBox('未开始')
        layout_tag3.addWidget(self.tag2_1, 1, 1)
        self.tag2_2 = QCheckBox('进行中')
        layout_tag3.addWidget(self.tag2_2, 1, 2)
        self.tag2_3 = QCheckBox('已完成')
        layout_tag3.addWidget(self.tag2_3, 1, 3)
        self.tag2_4 = QCheckBox('已过期')
        layout_tag3.addWidget(self.tag2_4, 1, 4)

        path="data\\" + global_user.getName() + "\\" + "tags.txt"
        f = open(path, "r")
        self.tag_init = f.read().split("\n")
        f.close()
        le = len(self.tag_init)
        self.tagNum = le
        self.tag3 = QLabel('类别: ')
        layout_tag3.addWidget(self.tag3, 2, 0)

        self.tag3_1 = QCheckBox(self.tag_init[0])
        layout_tag3.addWidget(self.tag3_1, 2, 1)

        self.tag3_2 = QCheckBox('2')
        if le > 1:
            self.tag3_2.setText(self.tag_init[1])
            layout_tag3.addWidget(self.tag3_2, 2, 2)
        self.tag3_3 = QCheckBox('3')
        if le > 2:
            self.tag3_3.setText(self.tag_init[2])
            layout_tag3.addWidget(self.tag3_3, 2, 3)
        self.tag3_4 = QCheckBox('4')
        if le > 3:
            self.tag3_4.setText(self.tag_init[3])
            layout_tag3.addWidget(self.tag3_4, 2, 4)
        self.tag3_5 = QCheckBox('5')
        if le > 4:
            self.tag3_5.setText(self.tag_init[4])
            layout_tag3.addWidget(self.tag3_5, 3, 1)
        self.tag3_6 = QCheckBox('6')
        if le > 5:
            self.tag3_6.setText(self.tag_init[5])
            layout_tag3.addWidget(self.tag3_6, 3, 2)
        self.tag3_7= QCheckBox('7')
        if le > 6:
            self.tag3_7.setText(self.tag_init[6])
            layout_tag3.addWidget(self.tag3_7, 3, 3)
        self.tag3_8 = QCheckBox('8')
        if le > 7:
            self.tag3_8.setText(self.tag_init[7])
            layout_tag3.addWidget(self.tag3_8, 3, 4)

        self.tag1_1.setChecked(True)
        self.tag1_2.setChecked(True)
        self.tag1_3.setChecked(True)
        self.tag1_4.setChecked(True)
        self.tag1_5.setChecked(True)
        self.tag2_1.setChecked(True)
        self.tag2_2.setChecked(True)
        self.tag2_3.setChecked(True)
        self.tag2_4.setChecked(True)
        self.tag3_1.setChecked(True)
        self.tag3_2.setChecked(True)
        self.tag3_3.setChecked(True)
        self.tag3_4.setChecked(True)
        self.tag3_5.setChecked(True)
        self.tag3_6.setChecked(True)
        self.tag3_7.setChecked(True)
        self.tag3_8.setChecked(True)

        self.tag1_1.clicked.connect((lambda:self.uploadDay()))
        self.tag1_2.clicked.connect((lambda: self.uploadDay()))
        self.tag1_3.clicked.connect((lambda: self.uploadDay()))
        self.tag1_4.clicked.connect((lambda: self.uploadDay()))
        self.tag1_5.clicked.connect((lambda: self.uploadDay()))
        self.tag2_1.clicked.connect((lambda: self.uploadDay()))
        self.tag2_2.clicked.connect((lambda: self.uploadDay()))
        self.tag2_3.clicked.connect((lambda: self.uploadDay()))
        self.tag2_4.clicked.connect((lambda: self.uploadDay()))
        self.tag3_1.clicked.connect((lambda: self.uploadDay()))
        self.tag3_2.clicked.connect((lambda: self.uploadDay()))
        self.tag3_3.clicked.connect((lambda: self.uploadDay()))
        self.tag3_4.clicked.connect((lambda: self.uploadDay()))
        self.tag3_5.clicked.connect((lambda: self.uploadDay()))
        self.tag3_6.clicked.connect((lambda: self.uploadDay()))
        self.tag3_7.clicked.connect((lambda: self.uploadDay()))
        self.tag3_8.clicked.connect((lambda: self.uploadDay()))

        self.listWidget33 = QtWidgets.QListWidget()
        layout_tag3.addWidget(self.listWidget33, 4, 0, 4, 6)
        self.listWidget33.setStyleSheet("#listWidget::item {\n"
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
        self.tag.setLayout(layout_tag3)
        ##################################################
        t3 = time.localtime()
        self.Year3 = t3.tm_year
        self.Month3 = t3.tm_mon

        self.layout_calendar3 = QGridLayout()  # 日历

        # 日历第一排
        blue3 = QtWidgets.QWidget()
        layout_blue3 = QGridLayout()

        self.label3_1 = QtWidgets.QLabel(self.tab3)  # 日历头蓝底
        self.label3_1.setStyleSheet("background:rgba(113, 113, 113,105)")
        layout_blue3.addWidget(self.label3_1, 0, 0, 1, 8)
        self.pushButton3_1 = QPushButton(self.tab3)  # 年份递减按钮
        self.pushButton3_1.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue3.addWidget(self.pushButton3_1, 0, 0)
        self.pushButton3_2 = QPushButton(self.tab3)  # 月份递减按钮
        self.pushButton3_2.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue3.addWidget(self.pushButton3_2, 0, 1)
        self.pushButton3_3 = QPushButton(self.tab3)  # 月份递增按钮
        self.pushButton3_3.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue3.addWidget(self.pushButton3_3, 0, 6)
        self.pushButton3_4 = QPushButton(self.tab3)  # 年份递增按钮
        self.pushButton3_4.setStyleSheet("background:rgba(113, 113, 113, 55)")
        layout_blue3.addWidget(self.pushButton3_4, 0, 7)
        self.label3_2 = QtWidgets.QLabel(self.tab3)  # 年份
        self.label3_2.setStyleSheet("background:rgba(113, 113, 113, 55)")
        self.label3_2.setAlignment(Qt.AlignCenter)
        layout_blue3.addWidget(self.label3_2, 0, 3)
        self.label3_3 = QtWidgets.QLabel(self.tab3)  # 月份
        self.label3_3.setStyleSheet("background:rgba(113, 113, 113, 55)")
        self.label3_3.setAlignment(Qt.AlignCenter)
        layout_blue3.addWidget(self.label3_3, 0, 4)

        self.label3_1.raise_()  # 蓝底
        self.pushButton3_1.raise_()  # 年份递减
        self.pushButton3_2.raise_()  # 月份递减
        self.pushButton3_3.raise_()  # 月份递增
        self.pushButton3_4.raise_()  # 年份递增
        self.label3_2.raise_()  # 年份
        self.label3_3.raise_()  # 月份

        blue3.setLayout(layout_blue3)
        self.layout_calendar3.addWidget(blue3, 0, 0)
        self.layout_calendar3.setRowStretch(0, 1)

        # 日历第二排
        white3 = QtWidgets.QWidget()
        layout_white3 = QGridLayout()
        self.label3_11 = QtWidgets.QLabel(self.tab3)  # 白底
        self.label3_11.setStyleSheet("background:rgba(255, 255, 255, 255)")
        self.label3_11.setText("")
        layout_white3.addWidget(self.label3_11, 0, 0, 1, 7)
        self.label3_4 = QtWidgets.QLabel(self.tab3)  # 周一
        self.label3_4.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_4.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_4, 0, 0)
        self.label3_5 = QtWidgets.QLabel(self.tab3)  # 周二
        self.label3_5.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_5.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_5, 0, 1)
        self.label3_6 = QtWidgets.QLabel(self.tab3)  # 周三
        self.label3_6.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_6.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_6, 0, 2)
        self.label3_7 = QtWidgets.QLabel(self.tab3)  # 周四
        self.label3_7.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_7.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_7, 0, 3)
        self.label3_8 = QtWidgets.QLabel(self.tab3)  # 周五
        self.label3_8.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_8.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_8, 0, 4)
        self.label3_9 = QtWidgets.QLabel(self.tab3)  # 周六
        self.label3_9.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_9.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_9, 0, 5)
        self.label3_10 = QtWidgets.QLabel(self.tab3)  # 周日
        self.label3_10.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label3_10.setAlignment(Qt.AlignCenter)
        layout_white3.addWidget(self.label3_10, 0, 6)
        self.label3_11 = QtWidgets.QLabel(self.tab3)  # 白底
        self.label3_11.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")

        self.label3_11.raise_()  # 白底
        self.label3_4.raise_()  # 周一
        self.label3_5.raise_()  # 周二
        self.label3_6.raise_()  # 周三
        self.label3_7.raise_()  # 周四
        self.label3_8.raise_()  # 周五
        self.label3_9.raise_()  # 周六
        self.label3_10.raise_()  # 周日

        white3.setLayout(layout_white3)
        self.layout_calendar3.addWidget(white3, 1, 0)
        self.layout_calendar3.setRowStretch(1, 1)
        ##################################################


        ##################################################
        # 一些显示和设置
        self.initCalender3()  # 显示周一到周日以及<<、<、>、>>

        self.date3 = []  # 31个日期按钮
        _translate = QtCore.QCoreApplication.translate
        for i in range(31):
            tmp = QPushButton(self.tab3)
            tmp.setText(_translate("MainWindow", str(i + 1)))
            self.date3.append(tmp)

        self.setPushButton3()  # 设置年份月份加减键、31个日期键对应的函数
        self.getImportance3()  # 获取重要性
        self.printCalender3()  # 打印日历
        ##################################################

        ##################################################
        # 日历按钮区
        button3 = QtWidgets.QWidget()
        layout_button3 = QGridLayout()

        # 提示语
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label3_12 = QLabel(self.tab3)
        self.label3_12.setText("当前没有日期被选中")
        self.label3_12.setAlignment(Qt.AlignCenter)
        self.label3_12.setFont(font)
        layout_button3.addWidget(self.label3_12, 1, 0, 1, 2)

        '''
        # 分析当前日期所在月份的数据按钮
        self.pushButton3_6 = QPushButton(self.tab3)
        self.pushButton3_6.setText(_translate("MainWindow", "Analyze the data of the selected month"))
        self.pushButton3_6.clicked.connect(lambda: self.analyze_month())# TODO
        layout_button3.addWidget(self.pushButton3_6, 2, 0, 1, 1)
        self.pushButton3_6.setObjectName("pushButton3_6")
        self.pushButton3_6.setFixedSize(400, 50)
        self.pushButton3_6.setText(_translate("MainWindow", "展示当前选择月份的数据分析"))
        self.pushButton3_6.clicked.connect(lambda: self.analyze_month())
        self.pushButton3_6.setStyleSheet("#pushButton_6{\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border: 3px solid rgb(0,0,0);\n"
                                        "    border-radius:10px\n"
                                        "}\n"
                                        "#pushButton_6:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#pushButton_6:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px\n"
                                        "}\n"
                                        "")

        # 分析当前日期所在周的数据按钮
        self.pushButton3_7 = QPushButton(self.tab3)
        self.pushButton3_7.setText(_translate("MainWindow", "Analyze the data of the selected week"))
        self.pushButton3_7.clicked.connect(lambda: self.analyze_week())
        layout_button3.addWidget(self.pushButton3_7, 2, 1, 1, 1)
        '''
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13 = QLabel(self.tab2)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setText(str(self.Year) + '/' + str(self.Month) + '/' + str(self.Day))
        self.label_14 = QLabel(self.tab3)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setText(str(self.Year) + '/' + str(self.Month) + '/' + str(self.Day))

        self.choosed_a_date3 = 0  # 当前还未选择一个日期
        button3.setLayout(layout_button3)
        self.layout_calendar3.addWidget(button3, 3, 0)
        self.layout_calendar3.setRowStretch(3, 3)
        ##################################################

        ##################################################
        # 添加日历布局
        cal3 = QtWidgets.QWidget()
        cal3.setLayout(self.layout_calendar3)
        self.top3 = QGridLayout()
        self.top3.addWidget(cal3, 0, 0)


        self.top3.addWidget(self.tag, 0, 1)  # 仅含文本的html布局
        #self.top3.setColumnStretch(4, 5)

        self.tab3.setLayout(self.top3)

    def initCalender(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("MainWindow", "<<"))
        self.pushButton_2.setText(_translate("MainWindow", "<"))
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.pushButton_4.setText(_translate("MainWindow", ">>"))
        self.label_4.setText(_translate("MainWindow", "Monday"))
        self.label_5.setText(_translate("MainWindow", "Tuesday"))
        self.label_6.setText(_translate("MainWindow", "Wednesday"))
        self.label_7.setText(_translate("MainWindow", "Thursday"))
        self.label_8.setText(_translate("MainWindow", "Friday"))
        self.label_9.setText(_translate("MainWindow", "Saturday"))
        self.label_10.setText(_translate("MainWindow", "Sunday"))

    # 设置4个pushButton、31个日期按钮对应的函数
    def setPushButton(self):
        self.pushButton_1.clicked.connect(lambda: self.printLastYear())
        self.pushButton_2.clicked.connect(lambda: self.printLastMonth())
        self.pushButton_3.clicked.connect(lambda: self.printNextMonth())
        self.pushButton_4.clicked.connect(lambda: self.printNextYear())
        # 31个日期按钮对应的函数
        self.date[0].clicked.connect((lambda: self.showDetails(1)))
        self.date[1].clicked.connect((lambda: self.showDetails(2)))
        self.date[2].clicked.connect((lambda: self.showDetails(3)))
        self.date[3].clicked.connect((lambda: self.showDetails(4)))
        self.date[4].clicked.connect((lambda: self.showDetails(5)))
        self.date[5].clicked.connect((lambda: self.showDetails(6)))
        self.date[6].clicked.connect((lambda: self.showDetails(7)))
        self.date[7].clicked.connect((lambda: self.showDetails(8)))
        self.date[8].clicked.connect((lambda: self.showDetails(9)))
        self.date[9].clicked.connect((lambda: self.showDetails(10)))
        self.date[10].clicked.connect((lambda: self.showDetails(11)))
        self.date[11].clicked.connect((lambda: self.showDetails(12)))
        self.date[12].clicked.connect((lambda: self.showDetails(13)))
        self.date[13].clicked.connect((lambda: self.showDetails(14)))
        self.date[14].clicked.connect((lambda: self.showDetails(15)))
        self.date[15].clicked.connect((lambda: self.showDetails(16)))
        self.date[16].clicked.connect((lambda: self.showDetails(17)))
        self.date[17].clicked.connect((lambda: self.showDetails(18)))
        self.date[18].clicked.connect((lambda: self.showDetails(19)))
        self.date[19].clicked.connect((lambda: self.showDetails(20)))
        self.date[20].clicked.connect((lambda: self.showDetails(21)))
        self.date[21].clicked.connect((lambda: self.showDetails(22)))
        self.date[22].clicked.connect((lambda: self.showDetails(23)))
        self.date[23].clicked.connect((lambda: self.showDetails(24)))
        self.date[24].clicked.connect((lambda: self.showDetails(25)))
        self.date[25].clicked.connect((lambda: self.showDetails(26)))
        self.date[26].clicked.connect((lambda: self.showDetails(27)))
        self.date[27].clicked.connect((lambda: self.showDetails(28)))
        self.date[28].clicked.connect((lambda: self.showDetails(29)))
        self.date[29].clicked.connect((lambda: self.showDetails(30)))
        self.date[30].clicked.connect((lambda: self.showDetails(31)))

    # 年份+1
    def printNextYear(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year += 1
        self.printCalender()

    # 年份-1
    def printLastYear(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year -= 1
        self.printCalender()

    # 月份+1
    def printNextMonth(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month += 1
        if self.Month == 13:
            self.Month = 1
            self.Year += 1
        self.printCalender()

    # 月份-1
    def printLastMonth(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month -= 1
        if self.Month == 0:
            self.Month = 12
            self.Year -= 1
        self.printCalender()

    def initCalender3(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton3_1.setText(_translate("MainWindow", "<<"))
        self.pushButton3_2.setText(_translate("MainWindow", "<"))
        self.pushButton3_3.setText(_translate("MainWindow", ">"))
        self.pushButton3_4.setText(_translate("MainWindow", ">>"))
        self.label3_4.setText(_translate("MainWindow", "周一"))
        self.label3_5.setText(_translate("MainWindow", "周二"))
        self.label3_6.setText(_translate("MainWindow", "周三"))
        self.label3_7.setText(_translate("MainWindow", "周四"))
        self.label3_8.setText(_translate("MainWindow", "周五"))
        self.label3_9.setText(_translate("MainWindow", "周六"))
        self.label3_10.setText(_translate("MainWindow", "周日"))

    # 设置4个pushButton、31个日期按钮对应的函数
    def setPushButton3(self):
        self.pushButton3_1.clicked.connect(lambda: self.printLastYear3())
        self.pushButton3_2.clicked.connect(lambda: self.printLastMonth3())
        self.pushButton3_3.clicked.connect(lambda: self.printNextMonth3())
        self.pushButton3_4.clicked.connect(lambda: self.printNextYear3())
        # 31个日期按钮对应的函数
        self.date3[0].clicked.connect((lambda: self.showDaily(1)))
        self.date3[1].clicked.connect((lambda: self.showDaily(2)))
        self.date3[2].clicked.connect((lambda: self.showDaily(3)))
        self.date3[3].clicked.connect((lambda: self.showDaily(4)))
        self.date3[4].clicked.connect((lambda: self.showDaily(5)))
        self.date3[5].clicked.connect((lambda: self.showDaily(6)))
        self.date3[6].clicked.connect((lambda: self.showDaily(7)))
        self.date3[7].clicked.connect((lambda: self.showDaily(8)))
        self.date3[8].clicked.connect((lambda: self.showDaily(9)))
        self.date3[9].clicked.connect((lambda: self.showDaily(10)))
        self.date3[10].clicked.connect((lambda: self.showDaily(11)))
        self.date3[11].clicked.connect((lambda: self.showDaily(12)))
        self.date3[12].clicked.connect((lambda: self.showDaily(13)))
        self.date3[13].clicked.connect((lambda: self.showDaily(14)))
        self.date3[14].clicked.connect((lambda: self.showDaily(15)))
        self.date3[15].clicked.connect((lambda: self.showDaily(16)))
        self.date3[16].clicked.connect((lambda: self.showDaily(17)))
        self.date3[17].clicked.connect((lambda: self.showDaily(18)))
        self.date3[18].clicked.connect((lambda: self.showDaily(19)))
        self.date3[19].clicked.connect((lambda: self.showDaily(20)))
        self.date3[20].clicked.connect((lambda: self.showDaily(21)))
        self.date3[21].clicked.connect((lambda: self.showDaily(22)))
        self.date3[22].clicked.connect((lambda: self.showDaily(23)))
        self.date3[23].clicked.connect((lambda: self.showDaily(24)))
        self.date3[24].clicked.connect((lambda: self.showDaily(25)))
        self.date3[25].clicked.connect((lambda: self.showDaily(26)))
        self.date3[26].clicked.connect((lambda: self.showDaily(27)))
        self.date3[27].clicked.connect((lambda: self.showDaily(28)))
        self.date3[28].clicked.connect((lambda: self.showDaily(29)))
        self.date3[29].clicked.connect((lambda: self.showDaily(30)))
        self.date3[30].clicked.connect((lambda: self.showDaily(31)))

    # 年份+1
    def printNextYear3(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year3 += 1
        self.printCalender3()

    # 年份-1
    def printLastYear3(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year3 -= 1
        self.printCalender3()

    # 月份+1
    def printNextMonth3(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month3 += 1
        if self.Month3 == 13:
            self.Month3 = 1
            self.Year3 += 1
        self.printCalender3()

    # 月份-1
    def printLastMonth3(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month3 -= 1
        if self.Month3 == 0:
            self.Month3 = 12
            self.Year3 -= 1
        self.printCalender3()

    def myFilter(self):
        self.IMPfilter=[]
        self.STATEfilter=[]
        self.TAGfilter=[]
        if self.tag1_1.isChecked():
            self.IMPfilter.append('1')
        if self.tag1_2.isChecked():
            self.IMPfilter.append('2')
        if self.tag1_3.isChecked():
            self.IMPfilter.append('3')
        if self.tag1_4.isChecked():
            self.IMPfilter.append('4')
        if self.tag1_5.isChecked():
            self.IMPfilter.append('5')

        if self.tag2_1.isChecked():
            self.STATEfilter.append('0')
        if self.tag2_2.isChecked():
            self.STATEfilter.append('1')
        if self.tag2_3.isChecked():
            self.STATEfilter.append('2')
        if self.tag2_4.isChecked():
            self.STATEfilter.append('3')

        le = self.tagNum
        if self.tag3_1.isChecked():
            self.TAGfilter.append(self.tag3_1.text())

        if le > 1:
            if self.tag3_2.isChecked():
                self.TAGfilter.append(self.tag3_2.text())

        if le > 2:
            if self.tag3_3.isChecked():
                self.TAGfilter.append(self.tag3_3.text())
        if le > 3:
            if self.tag3_4.isChecked():
                self.TAGfilter.append(self.tag3_4.text())
        if le > 4:
            if self.tag3_5.isChecked():
                self.TAGfilter.append(self.tag3_5.text())
        if le > 5:
            if self.tag3_6.isChecked():
                self.TAGfilter.append(self.tag3_6.text())
        if le > 6:
            if self.tag3_7.isChecked():
                self.TAGfilter.append(self.tag3_7.text())
        if le > 7:
            if self.tag3_8.isChecked():
                self.TAGfilter.append(self.tag3_8.text())

    def showDaily(self, i):
        #print("show daily")

        self.curYear3 = str(self.Year3)
        self.curMonth3 = str(self.Month3)
        self.curDay3 = str(i)

        # TODO
        if len(self.curMonth3) < 2:  # 补成两位数
            self.curMonth3 = "0" + self.curMonth3
        if len(self.curDay3) < 2:  # 补成两位数
            self.curDay3 = "0" + self.curDay3

        # TODO 找不到的日期文件

        path = "data\\" + global_user.getName() + "\\" + self.curYear3 + "\\" + self.curMonth3 + "\\" + self.curDay3 + ".txt"

        # 存在txt+\n，否则创建
        year_path = desk_path + global_user.getName() + '/' + str(self.curYear3)
        month_path = year_path + '/' + str(self.curMonth3)
        day_path = month_path + '/' + str(self.curDay3) + '.txt'

        self.dailyTxt = []

        if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
            if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                if os.path.exists(day_path):
                    f = open(day_path, 'r')
                    t = f.read()
                    if len(t):
                        self.dailyTxt = t.split('\n')

                    f.close()

        path="data\\" + global_user.getName() + "\\" + "routine.txt"
        f = open(path, "r")
        t = f.read()
        if len(t):

            self.dailyTxt.extend(t.split('\n'))
        f.close()
        if len(self.dailyTxt) == 0:
            return

        monthEnglish = ['0', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        # 提示成功选中该日期
        self.label3_12.setText("成功选中" + self.curYear3 + "年" + str(int(self.curMonth3)) + "月" + str(int(self.curDay3)) + "日")
        self.choosed_a_date3 = 1

        self.uploadDay()
        '''
        if not dic:  # dic为空
            #self.empty_html("There is no record on " + monthEnglish[int(self.curMonth)] + " " + str(int(self.curDay)) + ", " + self.curYear)
        else:

            self.top3.addWidget(self.day_pie, 0, 2)  # day-pie图表布局
            self.top3.setColumnStretch(2, 3)
        '''

    def getImportance3(self):
        # 这个 mpath应该是一个全局变量   在登陆后 设置为对应的用户所处的文件夹位置
        self.importance3 = {}
        Upath = "data\\" + global_user.getName()
        Ypaths = os.listdir(Upath)
        Ypaths = [Upath + "\\" + p for p in Ypaths]
        for Ypath in Ypaths:
            if not os.path.isdir(Ypath):
                continue
            year = os.path.basename(Ypath)
            Mpaths = os.listdir(Ypath)
            Mpaths = [Ypath + "\\" + p for p in Mpaths]
            for Mpath in Mpaths:
                month = os.path.basename(Mpath)
                Dpaths = os.listdir(Mpath)
                Dpaths = [Mpath + "\\" + p for p in Dpaths]
                for path in Dpaths:
                    day = os.path.basename(path).replace('.txt', '')
                    imp = self.get_imp(path)
                    date = '_'.join([year, month, day])
                    self.importance3[date] = imp

    #todo
    def printCalender3(self):
        _translate = QtCore.QCoreApplication.translate
        dates3 = QtWidgets.QWidget()
        layout_dates3 = QGridLayout()
        Calender = self.getDate(self.Year3, self.Month3)
        d = 0
        self.label3_2.setText(_translate("MainWindow", str(self.Year3) + "年"))
        self.label3_3.setText(_translate("MainWindow", str(self.Month3) + "月"))
        for i in self.date3:
            i.close()  # 关闭原来的日期显示
        for i in range(len(Calender)):
            for j in range(len(Calender[i])):
                if Calender[i][j] == 0:
                    continue
                else:
                    d += 1
                tmp = self.date3[d - 1]
                layout_dates3.addWidget(tmp, i, j)

                if len(str(self.Month3)) < 2:
                    _Month = "0" + str(self.Month3)
                else:
                    _Month = str(self.Month3)

                if len(str(d)) < 2:
                    _Day = "0" + str(d)
                else:
                    _Day = str(d)

                if self.importance3.__contains__('_'.join([str(self.Year3), _Month, _Day])):
                    imp = self.importance3['_'.join([str(self.Year3), _Month, _Day])]
                    if imp == 0:
                        tmp.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")
                    elif imp == 1:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 50)\n""")
                    elif imp == 2:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 100)\n""")
                    elif imp == 3:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 150)\n""")
                    elif imp == 4:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 200)\n""")
                    elif imp == 5:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 250)\n""")
                else:
                    tmp.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")

                tmp.raise_()
                tmp.show()

        dates3.setLayout(layout_dates3)
        self.layout_calendar3.addWidget(dates3, 2, 0)
        self.layout_calendar3.setRowStretch(2, 6)

    def initCalender(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("MainWindow", "<<"))
        self.pushButton_2.setText(_translate("MainWindow", "<"))
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.pushButton_4.setText(_translate("MainWindow", ">>"))
        self.label_4.setText(_translate("MainWindow", "周一"))
        self.label_5.setText(_translate("MainWindow", "周二"))
        self.label_6.setText(_translate("MainWindow", "周三"))
        self.label_7.setText(_translate("MainWindow", "周四"))
        self.label_8.setText(_translate("MainWindow", "周五"))
        self.label_9.setText(_translate("MainWindow", "周六"))
        self.label_10.setText(_translate("MainWindow", "周日"))

    # 设置4个pushButton、31个日期按钮对应的函数
    def setPushButton(self):
        self.pushButton_1.clicked.connect(lambda: self.printLastYear())
        self.pushButton_2.clicked.connect(lambda: self.printLastMonth())
        self.pushButton_3.clicked.connect(lambda: self.printNextMonth())
        self.pushButton_4.clicked.connect(lambda: self.printNextYear())
        # 31个日期按钮对应的函数
        self.date[0].clicked.connect((lambda: self.showDetails(1)))
        self.date[1].clicked.connect((lambda: self.showDetails(2)))
        self.date[2].clicked.connect((lambda: self.showDetails(3)))
        self.date[3].clicked.connect((lambda: self.showDetails(4)))
        self.date[4].clicked.connect((lambda: self.showDetails(5)))
        self.date[5].clicked.connect((lambda: self.showDetails(6)))
        self.date[6].clicked.connect((lambda: self.showDetails(7)))
        self.date[7].clicked.connect((lambda: self.showDetails(8)))
        self.date[8].clicked.connect((lambda: self.showDetails(9)))
        self.date[9].clicked.connect((lambda: self.showDetails(10)))
        self.date[10].clicked.connect((lambda: self.showDetails(11)))
        self.date[11].clicked.connect((lambda: self.showDetails(12)))
        self.date[12].clicked.connect((lambda: self.showDetails(13)))
        self.date[13].clicked.connect((lambda: self.showDetails(14)))
        self.date[14].clicked.connect((lambda: self.showDetails(15)))
        self.date[15].clicked.connect((lambda: self.showDetails(16)))
        self.date[16].clicked.connect((lambda: self.showDetails(17)))
        self.date[17].clicked.connect((lambda: self.showDetails(18)))
        self.date[18].clicked.connect((lambda: self.showDetails(19)))
        self.date[19].clicked.connect((lambda: self.showDetails(20)))
        self.date[20].clicked.connect((lambda: self.showDetails(21)))
        self.date[21].clicked.connect((lambda: self.showDetails(22)))
        self.date[22].clicked.connect((lambda: self.showDetails(23)))
        self.date[23].clicked.connect((lambda: self.showDetails(24)))
        self.date[24].clicked.connect((lambda: self.showDetails(25)))
        self.date[25].clicked.connect((lambda: self.showDetails(26)))
        self.date[26].clicked.connect((lambda: self.showDetails(27)))
        self.date[27].clicked.connect((lambda: self.showDetails(28)))
        self.date[28].clicked.connect((lambda: self.showDetails(29)))
        self.date[29].clicked.connect((lambda: self.showDetails(30)))
        self.date[30].clicked.connect((lambda: self.showDetails(31)))

    # 年份+1
    def printNextYear(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year += 1
        self.printCalender()

    # 年份-1
    def printLastYear(self):
        _translate = QtCore.QCoreApplication.translate
        self.Year -= 1
        self.printCalender()

    # 月份+1
    def printNextMonth(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month += 1
        if self.Month == 13:
            self.Month = 1
            self.Year += 1
        self.printCalender()

    # 月份-1
    def printLastMonth(self):
        _translate = QtCore.QCoreApplication.translate
        self.Month -= 1
        if self.Month == 0:
            self.Month = 12
            self.Year -= 1
        self.printCalender()

    # 打开某天的txt文件，返回记录有该天{类别:总时长}的字典dic
    def open_day_txt(self, path):
        dic = dict()
        try:
            f = open(path, "r", encoding="gbk")
            content = f.readline()
            while content != "":
                content = list(content.split(";"))
                cate = content[6]  # 获取该活动对应的类别
                # 保证为同一天
                start_time = content[2]  # hh:mm
                end_time = content[4]  # hh:mm
                time = cal_minute_duration(start_time, end_time)  # 获取活动的持续时间，单位为min
                if cate in dic:
                    dic[cate] += time
                else:
                    dic[cate] = time
                content = f.readline()
            return dic
        except OSError:  # 无法打开文件
            return dic

    # 显示每日任务+数据分析
    def showDetails(self, i):
        # 显示每日任务
        '''
        ui = details.Ui_Form()
        DetailWindow = QMainWindow()
        ui.setupUi(DetailWindow, self.Year, self.Month, i)
        DetailWindow.show()
        '''
        # 数据分析
        # 获取当前选中的年月日
        self.curYear = str(self.Year)
        self.curMonth = str(self.Month)
        self.curDay = str(i)

        if len(self.curMonth) < 2:  # 补成两位数
            self.curMonth = "0" + self.curMonth
        if len(self.curDay) < 2:  # 补成两位数
            self.curDay = "0" + self.curDay

        path = "data\\" + global_user.getName() + "\\" + self.curYear + "\\" + self.curMonth + "\\" + self.curDay + ".txt"

        # 读取日期文件
        dic = self.open_day_txt(path)
        # 读取日常文件
        tmp_dic = self.open_day_txt("data\\" + global_user.getName() + "\\" + "routine.txt")
        for key, value in tmp_dic.items():
            if key in dic:
                dic[key] += value
            else:
                dic[key] = value
        monthEnglish = ['0', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        # 提示成功选中该日期
        self.label_12.setText("成功选中" + self.curYear + "年" + str(int(self.curMonth)) + "月" + str(int(self.curDay)) + "日")
        self.choosed_a_date = 1
        if not dic:  # dic为空
            self.empty_html(self.curYear + "年" + str(int(self.curMonth)) + "月" + str(int(self.curDay)) + "日" + "无任何记录")
        else:
            self.day_pie = QWebEngineView()
            the_html_content = goto_creat_daypie_html(self.curYear + "年" + str(int(self.curMonth)) + "月" + str(int(self.curDay)) + "日", dic)
            self.day_pie.setHtml(the_html_content)
            self.top.addWidget(self.day_pie, 0, 2)  # day-pie图表布局
            self.top.setColumnStretch(2, 3)

    # 分析当前选中日期所在周的数据
    def analyze_week(self):
        # 未选择一个日期，则再次提示需要选择一个日期
        if self.choosed_a_date == 0:
            self.empty_html("没有日期被选中! 请点击左侧日历选择一个日期!")
            return

        # 之前已选择一个日期
        # 获取当前选中的年月日
        date_list = cal_date_to_week(self.curYear + "/" + self.curMonth + "/" + self.curDay)
        data = []  # 依次装入该周7天对应的7个字典
        # 读取一周7天文件+日常文件
        for day in date_list:
            day = day.replace("/", "\\")
            path = "data\\" + global_user.getName() + "\\" + day + ".txt"
            # 读取日期文件
            dic = self.open_day_txt(path)
            # 读取日常文件
            tmp_dic = self.open_day_txt("data\\" + global_user.getName() + "\\" + "routine.txt")
            for key, value in tmp_dic.items():
                if key in dic:
                    dic[key] += value
                else:
                    dic[key] = value
            data.append(dic)
        empty = 1  # 判断该周记录是否全为空
        for dic in data:
            if dic:
                empty = 0
                break
        if empty == 1:  # data里的7个字典均为空
            self.empty_html("当前选中周无任何记录")
        else:
            self.week_pie_line = QWebEngineView()
            the_html_content = goto_creat_week_pie_line_html(date_list, data)  # 传入7天date和data
            self.week_pie_line.setHtml(the_html_content)
            self.top.addWidget(self.week_pie_line, 0, 2)  # week-pie-line图表布局
            self.top.setColumnStretch(2, 3)

    # 分析当前选中日期所在月的数据
    def analyze_month(self):
        # 未选择一个日期，则再次提示需要选择一个日期
        if self.choosed_a_date == 0:
            self.empty_html("没有日期被选中! 请点击左侧日历选择一个日期!")
            return

        # 之前已选择一个日期
        # 获取当前选中的年月日
        date_list = cal_date_to_month(self.curYear + "/" + self.curMonth + "/" + self.curDay)
        data = []  # 依次装入该月所有天对应的各个字典
        # 读取一月文件+日常文件
        for day in date_list:
            day = day.replace("/", "\\")
            path = "data\\" + global_user.getName() + "\\" + day + ".txt"
            # 读取日期文件
            dic = self.open_day_txt(path)
            # 读取日常文件
            tmp_dic = self.open_day_txt("data\\" + global_user.getName() + "\\" + "routine.txt")
            for key, value in tmp_dic.items():
                if key in dic:
                    dic[key] += value
                else:
                    dic[key] = value
            data.append(dic)

        empty = 1  # 判断该月记录是否全为空
        for dic in data:
            if dic:
                empty = 0
                break
        if empty == 1:  # data里的所有字典均为空
            self.empty_html("当前选中月份无任何记录")
        else:
            self.month_bar = QWebEngineView()
            the_html_content = goto_creat_month_bar_html(date_list, data)  # 传入一个月的date和data
            self.month_bar.setHtml(the_html_content)
            self.top.addWidget(self.month_bar, 0, 2)  # month-bar图表布局
            self.top.setColumnStretch(2, 3)

    def get_imp(self, path):
        f = open(str(path), "r", encoding="gbk")
        lines = f.readlines()
        imp = 0
        for line in lines:
            items = line.split(';')
            imp = max(imp, int(items[5]))
        return imp

    def getImportance(self):
        # 这个 mpath应该是一个全局变量   在登陆后 设置为对应的用户所处的文件夹位置
        self.importance = {}
        Upath = "data\\" + global_user.getName()
        Ypaths = os.listdir(Upath)
        Ypaths = [Upath + "\\" + p for p in Ypaths]
        for Ypath in Ypaths:
            if not os.path.isdir(Ypath):
                continue
            year = os.path.basename(Ypath)
            Mpaths = os.listdir(Ypath)
            Mpaths = [Ypath + "\\" + p for p in Mpaths]
            for Mpath in Mpaths:
                month = os.path.basename(Mpath)
                Dpaths = os.listdir(Mpath)
                Dpaths = [Mpath + "\\" + p for p in Dpaths]
                for path in Dpaths:
                    day = os.path.basename(path).replace('.txt', '')
                    imp = self.get_imp(path)
                    date = '_'.join([year, month, day])
                    self.importance[date] = imp

    def getDate(self, year, month):
        return calendar.monthcalendar(year, month)

    #TODO
    def printCalender(self):#TODO
        _translate = QtCore.QCoreApplication.translate
        dates = QtWidgets.QWidget()
        layout_dates = QGridLayout()

        Calender = self.getDate(self.Year, self.Month)
        d = 0
        self.label_2.setText(_translate("MainWindow", str(self.Year) + "年"))
        self.label_3.setText(_translate("MainWindow", str(self.Month) + "月"))
        for i in self.date:
            i.close()  # 关闭原来的日期显示
        for i in range(len(Calender)):
            for j in range(len(Calender[i])):
                if Calender[i][j] == 0:
                    continue
                else:
                    d += 1
                tmp = self.date[d - 1]
                layout_dates.addWidget(tmp, i, j)

                if len(str(self.Month)) < 2:
                    _Month = "0" + str(self.Month)
                else:
                    _Month = str(self.Month)

                if len(str(d)) < 2:
                    _Day = "0" + str(d)
                else:
                    _Day = str(d)

                if self.importance.__contains__('_'.join([str(self.Year), _Month, _Day])):
                    imp = self.importance['_'.join([str(self.Year), _Month, _Day])]
                    if imp == 0:
                        tmp.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")
                    elif imp == 1:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 50)\n""")
                    elif imp == 2:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 100)\n""")
                    elif imp == 3:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 150)\n""")
                    elif imp == 4:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 200)\n""")
                    elif imp == 5:
                        tmp.setStyleSheet("background:rgba(" + self.color[self.colorflag] + ", 255)\n""")
                else:
                    tmp.setStyleSheet("background:rgba(255, 255, 255, 255)\n""")

                tmp.raise_()
                tmp.show()

        dates.setLayout(layout_dates)
        self.layout_calendar.addWidget(dates, 2, 0)
        self.layout_calendar.setRowStretch(2, 6)

    # content:要显示的文本
    # 生成仅含该文本的html并显示
    def empty_html(self, content):
        self.html = QWebEngineView()
        the_html_content = goto_creat_empty_html(content)
        self.html.setHtml(the_html_content)
        self.top.addWidget(self.html, 0, 2)  # 仅含文本的html布局
        self.top.setColumnStretch(2, 3)

    # 刷新函数
    def changed(self):
        self.getImportance()  # 获取重要性
        self.printCalender()  # 打印日历
        self.choosed_a_date = 0
        self.label_12.setText("当前没有日期被选中")
        self.empty_html("请点击左侧日历选择一个日期")  # 添加html布局
        #print("changed")

        self.getImportance3()  # 获取重要性
        self.printCalender3()  # 打印日历

        if self.choosed_a_date3:
            year_path = desk_path + global_user.getName() + '/' + str(self.curYear3)
            month_path = year_path + '/' + str(self.curMonth3)
            day_path = month_path + '/' + str(self.curDay3) + '.txt'
            self.dailyTxt = []

            if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
                if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                    if os.path.exists(day_path):
                        f = open(day_path, 'r')
                        t = f.read()
                        if len(t):
                            self.dailyTxt = t.split('\n')

                        f.close()
            path = "data\\" + global_user.getName() + "\\" + "routine.txt"
            f = open(path, "r")
            t = f.read()
            if len(t):
                self.dailyTxt.extend(t.split('\n'))
            f.close()
            if len(self.dailyTxt) == 0:
                return
            self.uploadDay()

    def setBackground(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgName == '':
            pass
        else:
            palette = QPalette()
            jpg = QtGui.QPixmap(imgName)
            pix = jpg.scaled(self.width(), self.height())
            palette.setBrush(QPalette.Background, QBrush(pix))
            self.setPalette(palette)
            f = open("用户背景信息.txt", 'a')
            f.write(global_user.getName() + ' ' + imgName + "\n")
            f.close()
            self.update()

    def resizeEvent(self, event):
        f = open('用户背景信息.txt')
        #print('back')
        lines = f.readlines()
        palette = QPalette()
        for line in lines:
            #print(line.split())
            if line.split()[0].__eq__(global_user.getName()):
                self.uploadimg = line.split(' ', 1)[1]
                #print(self.uploadimg)
                jpg = QtGui.QPixmap(line.split(' ', 1)[1].replace('\n', ''))
                #print(jpg)
                pix = jpg.scaled(self.width(), self.height())
                palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)
        QTabWidget.resizeEvent(self, event)

    def changeProfile(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgName == '':
            pass
        else:
            icon = QIcon(QPixmap(imgName).scaled(self.pushButton_8.rect().size()))
            self.pushButton_8.setIcon(icon)
            f = open("用户头像信息.txt", 'a')
            f.write( global_user.getName() + ' ' + imgName + "\n")
            f.close()

    def resizeWindow(self):
        if self.flag == 0:
            self.max_button.setToolTip('退出全屏')
            icon = QIcon(QPixmap('退出全屏.png').scaled(QSize(40, 40)))
            self.max_button.setIcon(icon)
            self.showFullScreen()
            self.flag = 1
        else:
            self.max_button.setToolTip('全屏')
            icon = QIcon(QPixmap('全屏.png').scaled(QSize(40, 40)))
            self.max_button.setIcon(icon)
            self.showNormal()
            self.flag = 0

    def initColor(self):
        f = open('用户背景色信息.txt')
        self.colorflag = -1
        lines = f.readlines()
        for line in lines:
            if line.split()[0].__eq__(global_user.getName()):
                self.colorflag = int(line.split()[1]) - 1
        f.close()
        self.changeColor()

    def changeColor(self):
        self.colorflag += 1
        self.colorflag = self.colorflag % 3
        self.pushButton_10.setStyleSheet('#pushButton_10 {border-radius:20px;background-color:rgba(' + self.color[self.colorflag] + ',255)};')
        self.printCalender()
        f = open("用户背景色信息.txt", 'a')
        f.write(global_user.getName() + ' ' + str(self.colorflag) + "\n")
        f.close()
        self.printCalender3()
        self.printCalender()

        #maind.window.change()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())
