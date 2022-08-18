import sys
import os
from calendar import weekday
from datetime import datetime, timedelta

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton, QTableWidgetItem, QTableWidget, \
    QWhatsThis

import global_user
from distribute import Ui_Dialogdd
from edit3 import *
from main_view import *
from in_dialog import *
from free_create import *
from new_tag import *
from routine import *
from edit1 import *
from edit4 import *
from var import *
from error import *
from error1 import *
from error2 import *
from error3 import *
from error4 import *
from error5 import *
from error6 import *
from error7 import *


btn_add_1 = []
btn_add_2 = []
btn_add_3 = []
btn_add_4 = []
btn_add_e1 = []
btn_add_e4 = []
# TODO 不在本周的任务，不显示
# cancel窗口 提示语 设置

n = datetime.now()
weekDate = []
weekPath = []
dateleft = 1 - int(n.strftime('%w'))
if dateleft == 1:
    dateleft = -6
for i in range(0, 7):
    ddd = i+dateleft
    dayStr = (n + timedelta(days=ddd)).strftime('%Y/%m/%d')
    weekPath.append(dayStr)
    weekDate.append(dayStr.split("/"))

table = {}
wholeTable = {}

split_list = []
routine_list = []

p = []
pindex = 0

dele_text = ''

global_row = -1
global_col = -1


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_view = Ui_MainWindowxx()
        self.main_view.setupUi(self)

        for i in range(0, 7):
            for j in range(0, 12):
                self.main_view.tableWidget.setItem(j, i, QTableWidgetItem(''))




        #self.initRoutine()
        #self.initTable()
        #self.initToDo()

    def change1(self):


        global table
        table = {}
        global wholeTable
        wholeTable = {}
        for i in range(0, 7):
            for j in range(0, 12):
                self.main_view.tableWidget.setItem(j, i, QTableWidgetItem(''))
        global n
        global weekDate
        global weekPath
        global dateleft
        n = n+ timedelta(days=-7)
        weekDate = []
        weekPath = []
        dateleft = 1 - int(n.strftime('%w'))
        if dateleft == 1:
            dateleft = -6


        for i in range(0, 7):
            ddd = i + dateleft
            dayStr = (n + timedelta(days=ddd)).strftime('%Y/%m/%d')
            weekPath.append(dayStr)
            weekDate.append(dayStr.split("/"))

        for d in weekPath:
            start_day=d.split('/')
            year_path = desk_path + global_user.getName() + '/' + start_day[0]
            month_path = year_path + '/' + start_day[1]
            day_path = month_path + '/' + start_day[2] + '.txt'
            if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
                if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                    if os.path.exists(day_path):
                        f = open(day_path, 'r')

                        f.close()
                    else:
                        f = open(day_path, 'w')
                        f.close()
                else:  # 桌面文件夹存在，子文件夹不存在，则创建
                    os.mkdir(month_path)  # 创建子文件夹
                    f = open(day_path, 'w')
                    f.close()
            else:  # 桌面文件夹不存在，则创建桌面文件夹和子文件夹
                os.mkdir(year_path)  # 创建桌面文件夹
                os.mkdir(month_path)
                f = open(day_path, 'w')
                f.close()

        for i in range(0, 7):
            for j in range(0, 12):
                self.main_view.tableWidget.setItem(j, i, QTableWidgetItem(''))

        item = window.main_view.tableWidget.horizontalHeaderItem(0)
        item.setText("MON" + '\n' + weekPath[0])
        item = window.main_view.tableWidget.horizontalHeaderItem(1)
        item.setText("TUE" + '\n' + weekPath[1])
        item = window.main_view.tableWidget.horizontalHeaderItem(2)
        item.setText("WED" + '\n' + weekPath[2])
        item = window.main_view.tableWidget.horizontalHeaderItem(3)
        item.setText("TUR" + '\n' + weekPath[3])
        item = window.main_view.tableWidget.horizontalHeaderItem(4)
        item.setText("FRI" + '\n' + weekPath[4])
        item = window.main_view.tableWidget.horizontalHeaderItem(5)
        item.setText("SAT" + '\n' + weekPath[5])
        item = window.main_view.tableWidget.horizontalHeaderItem(6)
        item.setText("SUN" + '\n' + weekPath[6])

        self.initRoutine()
        self.initTable()
        #self.initToDo()

    def change2(self):
        global table
        table = {}
        global wholeTable
        wholeTable = {}
        for i in range(0, 7):
            for j in range(0, 12):
                self.main_view.tableWidget.setItem(j, i, QTableWidgetItem(''))
        global n
        global weekDate
        global weekPath
        global dateleft
        n = n+ timedelta(days=7)
        weekDate = []
        weekPath = []
        dateleft = 1 - int(n.strftime('%w'))
        if dateleft == 1:
            dateleft = -6
        for i in range(0, 7):
            ddd = i + dateleft
            dayStr = (n + timedelta(days=ddd)).strftime('%Y/%m/%d')
            weekPath.append(dayStr)
            weekDate.append(dayStr.split("/"))

        for d in weekPath:
            start_day = d.split('/')
            year_path = desk_path + global_user.getName() + '/' + start_day[0]
            month_path = year_path + '/' + start_day[1]
            day_path = month_path + '/' + start_day[2] + '.txt'
            if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
                if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                    if os.path.exists(day_path):
                        f = open(day_path, 'r')

                        f.close()
                    else:
                        f = open(day_path, 'w')
                        f.close()
                else:  # 桌面文件夹存在，子文件夹不存在，则创建
                    os.mkdir(month_path)  # 创建子文件夹
                    f = open(day_path, 'w')
                    f.close()
            else:  # 桌面文件夹不存在，则创建桌面文件夹和子文件夹
                os.mkdir(year_path)  # 创建桌面文件夹
                os.mkdir(month_path)
                f = open(day_path, 'w')
                f.close()

        for i in range(0, 7):
            for j in range(0, 12):
                self.main_view.tableWidget.setItem(j, i, QTableWidgetItem(''))

        item = window.main_view.tableWidget.horizontalHeaderItem(0)
        item.setText("MON" + '\n' + weekPath[0])
        item = window.main_view.tableWidget.horizontalHeaderItem(1)
        item.setText("TUE" + '\n' + weekPath[1])
        item = window.main_view.tableWidget.horizontalHeaderItem(2)
        item.setText("WED" + '\n' + weekPath[2])
        item = window.main_view.tableWidget.horizontalHeaderItem(3)
        item.setText("TUR" + '\n' + weekPath[3])
        item = window.main_view.tableWidget.horizontalHeaderItem(4)
        item.setText("FRI" + '\n' + weekPath[4])
        item = window.main_view.tableWidget.horizontalHeaderItem(5)
        item.setText( "SAT" + '\n' + weekPath[5])
        item = window.main_view.tableWidget.horizontalHeaderItem(6)
        item.setText("SUN" + '\n' + weekPath[6])

        self.initRoutine()
        self.initTable()
        #self.initToDo()


    def cfgItemChanged(self, row, column):
        # 获取更改内容
        cfgValue = self.main_view.tableWidget.item(row, column).text()

    def addTable(self, start_hour, day_index, text):
        item = (start_hour, day_index)  # TODO 星期几

        self.main_view.tableWidget.item(int(start_hour),int(day_index)).setText('\n'.join(table[item]))
        global global_row
        global global_col

        if global_row != -1:
            k = (global_row, global_col)
            self.main_view.listWidget.clear()
            if k in table:
                x = table[k]
                for i in range(0, len(x)):
                    self.main_view.listWidget.addItem(QtWidgets.QListWidgetItem(x[i]))

    def addToDo(self):
        self.main_view.listWidget_2.clear()
        if len(split_list):
            split_list.sort(key=lambda x: (x[0]))

            for i in split_list:
                self.main_view.listWidget_2.addItem(QtWidgets.QListWidgetItem(i[0]+' '+i[1][0]))
        f = open(desk_path + global_user.getName()+ '/' + 'ToDo.txt', "w")
        if len(split_list):
            f.write(';'.join(split_list[0][1]))
            for i in range(1, len(split_list)):
                f.write('\n')
                f.write(';'.join(split_list[i][1]))
        f.close()

    def cfgItemShowed(self, row, column):

        global global_col
        global_col = column
        global global_row
        global_row=row
        k = (row, column)
        self.main_view.listWidget.clear()
        if k in table:
            x = table[k]

            for i in range(0, len(x)):
                self.main_view.listWidget.addItem(QtWidgets.QListWidgetItem(x[i]))

    def initToDo(self):
        f = open(desk_path + global_user.getName()+'/'+"ToDo.txt", "r")
        t = f.read()
        if len(t) == 0:
            return
        todo_list = t.split("\n")
        for i in range(0, len(todo_list)):
            p = todo_list[i].split(";")
            split_list.append((p[3]+" "+p[4], p))
        f.close()
        split_list.sort(key=lambda x: (x[0]))
        for i in split_list:
            self.main_view.listWidget_2.addItem(QtWidgets.QListWidgetItem(i[0]+' '+i[1][0]))

    def initTable(self):
        for d in weekPath:

            day_path = desk_path + global_user.getName() + '/' + d + '.txt'
            if os.path.exists(day_path):
                f = open(day_path, "r")
                t = f.read()
                if len(t) == 0:
                    for item in table.items():
                        self.main_view.tableWidget.item((item[0][0]), (item[0][1])).setText('\n'.join(item[1]))
                    continue
                day_list = t.split("\n")

                for i in day_list:
                    items = i.split(";")
                    #print(i)
                    start_hour = ((int)(items[2].split(":")[0]))//2
                    start_day = items[1].split("/")
                    #print(start_day)
                    day_index = weekday(int(start_day[0]), int(start_day[1]), int(start_day[2]))

                    item = (start_hour, day_index)

                    if item not in table:
                        table[item] = []
                        wholeTable[item] = []
                    table[item].append(items[2] + " " + items[0])
                    wholeTable[item].append(items)

        for item in table.items():
            self.main_view.tableWidget.item((item[0][0]), (item[0][1])).setText('\n'.join(item[1]))



    def initRoutine(self):
        f = open(desk_path + global_user.getName()+'/'+"routine.txt", "r")
        t = f.read()
        f.close()
        if len(t) == 0:
            return

        day_list = t.split("\n")

        routine_list.extend(day_list)
        for i in day_list:
            items = i.split(";")
            start_hour = ((int)(items[2].split(":")[0])) // 2

            for i in range(0, 7):
                item = (start_hour, i)

                if item not in table:
                    table[item]=[]
                    wholeTable[item]=[]
                table[item].append(items[2] + " " + items[0])
                wholeTable[item].append(items)

    #文件+显示
    def addRoutine(self, start_hour, text, l):
        f = open(desk_path + global_user.getName()+'/'+"routine.txt", "a")
        if len(routine_list):
            f.write('\n')
        f.write(';'.join(l))
        f.close()
        routine_list.append(';'.join(l))

        for i in range(0, 7):
            item = (start_hour, i)
            if item not in table:
                table[item] = []
                wholeTable[item] = []
            table[item].append(text)
            wholeTable[item].append(l)
            self.main_view.tableWidget.item(int(start_hour), int(i)).setText('\n'.join(table[item]))

    ###文件+显示
    def deleRoutine(self, old_start_hour, old_text, old_l):

        global p

        strp=';'.join(p)
        #print(strp)

        routine_list.remove(strp)

        f = open(desk_path + global_user.getName()+ '/' + "routine.txt", "r")
        day_list = f.read().split("\n")
        f.close()
        day_list.remove(strp)

        f = open(desk_path + global_user.getName()+ '/' + "routine.txt", "w")
        if len(day_list):
            f.write(day_list[0])
        for i in range(1, len(day_list)):
            f.write('\n'+day_list[i])
        f.close()

        #TODO 不要加一样的事件
        for i in range(0, 7):
            item = (old_start_hour, i)
            table[item].remove(old_text)
            wholeTable[item].remove(old_l)
            self.main_view.tableWidget.item(int(old_start_hour), int(i)).setText('\n'.join(table[item]))

    def toDoItemShowedx(self, inde):
        index = self.main_view.listWidget_2.row(inde)
        global p
        p = split_list[index][1]
        global pindex
        pindex = index
        child2_edit.show()

    def itemShowedx(self, inde):
        index = self.main_view.listWidget.row(inde)

        global p
        global global_row
        global global_col
        p = wholeTable[(global_row, global_col)][index]
        global pindex
        pindex = index
        global dele_text

        dele_text = window.main_view.listWidget.item(index).text()
        if p[1] == '':
            child4_edit.show()
        else:
            child1_edit.show()


class distriWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.distri = Ui_Dialogdd()
        self.distri.setupUi(self)
        self.distri.buttonBox.accepted.connect(self.accept)
        self.distri.buttonBox.rejected.connect(self.reject)

    def accept(self):
        disDay = self.distri.dateEdit.text()
        start_day = disDay.split('/')

        has = 0
        year_path = desk_path + global_user.getName() + '/' + start_day[0]
        month_path = year_path + '/' + start_day[1]
        day_path = month_path + '/' + start_day[2] + '.txt'
        if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
            if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                if os.path.exists(day_path):
                    f = open(day_path, 'r')
                    if len(f.read()):
                        has = 1
                    f.close()
                else:
                    f = open(day_path, 'w')
                    f.close()
            else:  # 桌面文件夹存在，子文件夹不存在，则创建
                os.mkdir(month_path)  # 创建子文件夹
                f = open(day_path, 'w')
                f.close()
        else:  # 桌面文件夹不存在，则创建桌面文件夹和子文件夹
            os.mkdir(year_path)  # 创建桌面文件夹
            os.mkdir(month_path)
            f = open(day_path, 'w')
            f.close()

        k = split_list
        if self.distri.radioButton_2.isChecked():
            k.sort(key=lambda x: ((-int(x[1][5])), x[0]))

        timestrTable = []
        f = open(desk_path + global_user.getName()+ '/' + "routine.txt", "r")
        h = f.read()

        f.close()
        if len(h):
            timestrTable.extend(h.split("\n"))

        nowTime = datetime.strptime('08:00', "%H:%M")
        closeTime = datetime.strptime('23:00', "%H:%M")
        bre = timedelta(minutes=int(10))
        tmp = []
        memRem = -1

        if has:
            f = open(day_path, 'r')
            timestrTable.extend(f.read().split('\n'))
            f.close()
        timestrTable.append('lunch;xx;12:00;;13:50;5;eating;;0')
        timestrTable.append('dinner;xx;18:00;;18:50;5;eating;;0')

        timeTable = []
        for s in timestrTable:
            timeTable.append(s.split(';'))

        #print(timeTable)

        timeTable.sort(key=lambda x: (x[2]))
        nowIndex = 0
        end = 0  # 事件遍历结束
        leng = len(timeTable)
        while timeTable[nowIndex][4] < '08:00':
            nowIndex += 1
            if nowIndex == leng:
                end = 1
                break
        # start  8/item_end
        if end == 0:
            if timeTable[nowIndex][2] < '08:00':
                nowTime = datetime.strptime(timeTable[nowIndex][4], "%H:%M")+timedelta(minutes=int(10))
                nowIndex += 1
                if nowIndex == leng:
                    end = 1

        # end  24/item_start
        if end == 0:
            closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")
            while closeTime.strftime("%H:%M") <= nowTime.strftime("%H:%M"):
                nowTime = datetime.strptime(timeTable[nowIndex][4], "%H:%M") + bre
                nowIndex += 1

                if nowIndex == leng:
                    end = 1
                    closeTime = datetime.strptime('23:00', "%H:%M")
                    break
                closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")

        while True:
            if closeTime.strftime("%H:%M") <= nowTime.strftime("%H:%M"):
                break
            memRem = -1
            for i in range(0, len(k)):
                todol = k[i]
                lastTime = todol[1][2].split(':')
                de = timedelta(hours=int(lastTime[0]), minutes=int(lastTime[1]))

                startTime = nowTime.strftime("%H:%M")
                endTime = (nowTime + de).strftime("%H:%M")
                if (endTime <= closeTime.strftime("%H:%M")) and (endTime > startTime):

                    l = [todol[1][0], disDay, startTime, disDay, endTime, todol[1][5], todol[1][6], todol[1][7], todol[1][8]]
                    tmp.append(l)
                    nowTime = nowTime + de+bre
                    memRem = i

                    # 刷新新的closeTime
                    if end == 0:
                        # closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")
                        while closeTime.strftime("%H:%M") <= nowTime.strftime("%H:%M"):
                            nowTime = datetime.strptime(timeTable[nowIndex][4], "%H:%M") + bre
                            nowIndex += 1
                            if nowIndex == leng:
                                end = 1
                                closeTime = datetime.strptime('23:00', "%H:%M")
                                break
                            closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")
                    else:
                        closeTime = datetime.strptime('23:00', "%H:%M")

                    # 找到，退出
                    break

            # 当前nowtime间隔塞下了一个事情
            if memRem != -1:
                k.pop(memRem)
                if len(k) == 0:
                    break
            # 当前间隔太小了，找到下一个时间间隔换
            else:
                if end == 0:
                    nowTime = datetime.strptime(timeTable[nowIndex][4], "%H:%M") + bre
                    nowIndex += 1
                    if nowIndex == leng:
                        end = 1
                        closeTime = datetime.strptime('23:00', "%H:%M")
                    else:
                        closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")
                else:
                    break
                    # 当前间隔太小了，无法满足事情

                # 换间隔
                if end == 0:
                    while closeTime.strftime("%H:%M") <= nowTime.strftime("%H:%M"):
                        nowTime = datetime.strptime(timeTable[nowIndex][4], "%H:%M") + bre
                        nowIndex += 1
                        if nowIndex == leng:
                            end = 1
                            closeTime = datetime.strptime('23:00', "%H:%M")
                            break
                        closeTime = datetime.strptime(timeTable[nowIndex][2], "%H:%M")
        #print(tmp)

        f = open(desk_path + global_user.getName()+'/' + 'ToDo.txt', "w")
        f.close()
        window.main_view.listWidget_2.clear()
        # split_list = k
        #print(split_list)
        #print(k)

        if len(k):

            split_list.sort(key=lambda x: (x[0]))

            for i in split_list:
                window.main_view.listWidget_2.addItem(QtWidgets.QListWidgetItem(i[0] + ' ' + i[1][0]))
            f = open(desk_path + global_user.getName() + '/' + 'ToDo.txt', "w")
            if len(split_list):
                f.write(';'.join(split_list[0][1]))
                for i in range(1, len(split_list)):
                    f.write('\n')
                    f.write(';'.join(split_list[i][1]))
            f.close()

        # window.initToDo()

        c = weekday(int(start_day[0]), int(start_day[1]), int(start_day[2]))

        timeTable.extend(tmp)
        check_list=[]
        for m in timeTable:
            if m[1] != 'xx':
                check_list.append(m)

        check_list.sort(key=lambda x: (x[2]))

        ### 表格 全局变量 更新
        for i in range(0, 12):
            table[(i, c)] = []
            wholeTable[(i, c)] = []

        for i in check_list:
            item = (int(i[2].split(":")[0]) // 2, c)

            table[item].append(i[2] + " " + i[0])
            wholeTable[item].append(i)

        ### 主视图 表格 更新为 全局变量有序
        for r in range(0,12):
            window.addTable(r, c, '')

        check_list_r = []
        for k in check_list:
            if len(k[1]):
                check_list_r.append(k)

        ### 文件更新为排序后的
        f = open(day_path, "w")
        if len(check_list_r):
            f.write(';'.join(check_list_r[0]))
            for k in range(1, len(check_list_r)):
                f.write('\n' + ';'.join(check_list_r[k]))
        f.close()

        self.close()

    def show(self):
        QDialog.show(self)


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.in_dialog = Ui_Dialog()
        self.in_dialog.setupUi(self)
        self.in_dialog.buttonBox_2.accepted.connect(self.accept)
        self.in_dialog.buttonBox_2.rejected.connect(self.reject)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def accept(self):
        title = self.in_dialog.lineEdit_2.text()
        s = self.in_dialog.dateTimeEdit.text()
        e = self.in_dialog.dateTimeEdit_2.text()
        start = s.split(" ")
        end = e.split(" ")
        #if start[0] != end[0]:
        #    return
        start_day = start[0].split('/')
        start_time = start[1].split(":")
        end_day = end[0].split('/')
        end_time = end[1]
        importance = self.in_dialog.spinBox.currentText()
        tag = self.in_dialog.comboBox.currentText()
        attach = self.in_dialog.lineEdit.text()

        if s>=e:  # TODO 起始时间大于结束时间 error1
            #global nowstr
            #nowstr = error1
            errorSymbol1.show()
            self.close()
            return

        if start[0] != end[0]:  # TODO error2
            #global nowstr
            #nowstr = error1
            errorSymbol2.show()
            self.close()
            return

        # 存在txt+\n，否则创建
        year_path = desk_path + global_user.getName()+'/'+start_day[0]
        month_path = year_path+'/'+start_day[1]
        day_path = month_path+'/'+start_day[2]+'.txt'
        if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
            if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                if os.path.exists(day_path):
                    f = open(day_path, 'a')

                    f.close()
                else:
                    f = open(day_path, 'w')
                    f.close()
            else:  # 桌面文件夹存在，子文件夹不存在，则创建
                os.mkdir(month_path)  # 创建子文件夹
                f = open(day_path, 'w')
                f.close()
        else:  # 桌面文件夹不存在，则创建桌面文件夹和子文件夹
            os.mkdir(year_path)  # 创建桌面文件夹
            os.mkdir(month_path)
            f = open(day_path, 'w')
            f.close()

        r = int(start_time[0]) // 2
        c = weekday(int(start_day[0]), int(start_day[1]), int(start_day[2]))
        l = [title, str(start[0]), str(start[1]), str(end[0]), str(end[1]), importance, tag, attach, str(0)]  # TODO 完成情况

        f = open(day_path, "r")
        m = f.read()
        f.close()

        global global_row
        global global_col
        global p
        ### 空文件，不比较时间重叠，不加\n
        if len(m) == 0:
            ### 文件更新为排序后的
            f = open(day_path, "w")
            f.write(';'.join(l))
            f.close()
            ### 表格 全局变量 更新
            #for i in range(0,12):
            #    table[(i,c)] = []
            #    wholeTable[(i, c)] = []

            #item = (global_row,global_col)
            #table[item].remove(p)
            #window.addTable(global_row, global_col, p[1] + " " + p[0])
            if start[0] in weekPath:
                item = (r, c)
                if item not in table:
                    table[item] = []
                    wholeTable[item] = []

                table[item].append(str(l[2]) + " " + str(l[0]))
                wholeTable[item].append(l)
                ### 主视图 表格 更新为 全局变量有序
                window.addTable(r, c,  start[1]+" " + title)
            self.close()
            return

        ### 比较时间重叠，写入文件
        check = m.split("\n")
        check_list = []
        #print(check)
        for k in check:
            check_list.append(k.split(";"))

        f = open(desk_path + global_user.getName() + '/' + "routine.txt", "r")
        h = f.read()
        f.close()
        if len(h):
            day_list = h.split("\n")

            for k in day_list:
                check_list.append(k.split(";"))

        check_list.append(l)

        #print(check_list)
        check_list.sort(key=lambda x: (x[2]))

        i = check_list.index(l)
        x1 = True
        x2 = True
        if i:
            x1 = (check_list[i-1][4] < start[1])
        if i < (len(check_list)-1):
            x2 = (end[1] < check_list[i+1][2])
        if (x1 and x2):
            ### 文件更新为排序后的
            f = open(day_path, "w")
            flag_return = 0

            for k in range(0, len(check_list)):
                if len(check_list[k][1]):
                    if flag_return:
                        f.write('\n' + ';'.join(check_list[k]))
                    else:
                        f.write(';'.join(check_list[k]))
                        flag_return = 1
            f.close()

            if start[0] in weekPath:
                ### 表格 全局变量 更新
                for i in range(0, 12):
                    table[(i, c)] = []
                    wholeTable[(i, c)] = []

                for i in check_list:
                    item = (int(i[2].split(":")[0]) // 2, c)

                    table[item].append(i[2] + " " + i[0])
                    wholeTable[item].append(i)

                ### 主视图 表格 更新为 全局变量有序
                window.addTable(r, c, title + " " + start[1])
            self.close()
        else:
            # nowstr
            #nowstr=error4
            errorSymbol4.show()
            self.close()
            #pass  # TODO 时间重叠 error4

    def show(self):
        if len(btn_add_1):
            self.in_dialog.comboBox.addItems(btn_add_1)
            btn_add_1.clear()
        QDialog.show(self)


class editWindow1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.edit1 = Ui_Dialog11()
        self.edit1.setupUi(self)
        self.edit1.label.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                        "border-radius: 4px;                                             \n"
                                        "color: rgb(255, 255, 255);        \n"
                                        "background-color: rgb(198, 198, 198);")
        self.edit1.label_2.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                        "border-radius: 4px;                                             \n"
                                        "color: rgb(255, 255, 255);        \n"
                                        "background-color: rgb(198, 198, 198);")
        self.edit1.buttonBox_2.accepted.connect(self.accept)
        self.edit1.buttonBox_2.rejected.connect(self.rejectt)

    def accept(self):
        global pindex
        title = self.edit1.lineEdit_2.text()
        s = self.edit1.dateTimeEdit.text()
        e = self.edit1.dateTimeEdit_2.text()
        start = s.split(" ")
        end = e.split(" ")
        if s >= e:  # TODO 起始时间大于结束时间 error1
            # global nowstr
            # nowstr = error1
            errorSymbol1.show()
            self.close()
            return

        if start[0] != end[0]:  # TODO error2
            # global nowstr
            # nowstr = error1
            errorSymbol2.show()
            self.close()
            return
        start_day = start[0].split('/')
        start_time = start[1].split(":")
        end_day = end[0].split('/')
        end_time = end[1]
        importance = self.edit1.spinBox.currentText()
        tag = self.edit1.comboBox.currentText()
        attach = self.edit1.lineEdit.text()
        state = 0
        if self.edit1.radioButton.isChecked():
            state = 0
        elif self.edit1.radioButton_2.isChecked():
            state = 1
        elif self.edit1.radioButton_3.isChecked():
            state = 2
        else:
            state = 3
        '''
        if s>=e:  #TODO 起始时间大于结束时间
            #global nowstr
            #nowstr = error1
            errorSymbol.show()
            self.close()
            return
        '''
        global p



        day_path = desk_path + global_user.getName() + '/' + p[1] + '.txt'

        f = open(day_path, "r")
        check = f.read().split('\n')
        f.close()
        check.remove(';'.join(p))
        f = open(day_path, "w")
        length = len(check)
        if length:
            f.write(check[0])
        for ii in range(1, length):
            f.write('\n' + check[ii])
        f.close()


        # 一定存在txt
        year_path = desk_path + global_user.getName() + '/' + start_day[0]
        month_path = year_path + '/' + start_day[1]
        day_path = month_path+ '/' + start_day[2] + '.txt'

        r = int(start_time[0]) // 2
        c = weekday(int(start_day[0]), int(start_day[1]), int(start_day[2]))
        l = [title, str(start[0]), str(start[1]), str(end[0]), str(end[1]), importance, tag, attach, str(state)]  # TODO 完成情况



        f = open(day_path, "r")
        check = f.read().split('\n')
        f.close()


        ### 空文件，不比较时间重叠，不加\n
        if len(check) == 1:
            ### 文件更新为排序后的
            f = open(day_path, "w")
            f.write(';'.join(l))
            f.close()
            ### 表格 全局变量 更新
            item = (global_row, global_col)
            table[item].remove(dele_text)
            wholeTable[item].remove(p)
            window.addTable(global_row, global_col, p[1] + " " + p[0])
            item = (r, c)
            if item not in table:
                table[item] = []
                wholeTable[item] = []

            table[item].append(str(l[2]) + " " + str(l[0]))
            wholeTable[item].append(l)
            ### 主视图 表格 更新为 全局变量有序
            window.addTable(r, c, title + " " + start[1])
            self.close()
            return

        ### 比较时间重叠，写入文件

        check_list = []
        for k in check:
            check_list.append(k.split(";"))

        #check_list.remove(p)
        #移除旧的

        f = open(desk_path + global_user.getName() + '/' + "routine.txt", "r")
        h = f.read()
        f.close()
        if len(h):
            day_list = h.split("\n")

            for k in day_list:
                check_list.append(k.split(";"))

        check_list.append(l)

        #加入新的
        check_list.sort(key=lambda x: (x[2]))

        i = check_list.index(l)
        x1 = True
        x2 = True
        if i:
            x1 = (check_list[i-1][4] < start[1])

        if i < (len(check_list)-1):
            x2 = (end[1] < check_list[i+1][2])
        if (x1 and x2):
            ### 文件更新为排序后的
            f = open(day_path, "w")
            flag_return = 0

            for k in range(0, len(check_list)):
                if len(check_list[k][1]):
                    if flag_return:
                        f.write('\n' + ';'.join(check_list[k]))
                    else:
                        f.write(';'.join(check_list[k]))
                        flag_return = 1
            f.close()

            ### 表格 全局变量 更新
            for i in range(0, 12):
                table[(i, c)] = []

                wholeTable[(i, c)] = []

            for i in check_list:
                item = (int(i[2].split(":")[0]) // 2, c)

                table[item].append(i[2] + " " + i[0])
                wholeTable[item].append(i)

            ### 主视图 表格 更新为 全局变量有序
            window.addTable(r, c, title + " " + start[1])
            self.close()



        else:
            #文件和视图都不改
            #global nowstr
            #nowstr = error4
            errorSymbol4.show()
            self.close()

    def rejectt(self):
        global pindex
        global global_row
        global global_col
        global p

        k = (global_row, global_col)

        table[k].pop(pindex)

        wholeTable[k].remove(p)

        ### 全局变量删除 主视图更新
        window.addTable(global_row, global_col, '')

        # 一定存在txt
        day_path = desk_path + global_user.getName() + '/' + p[1] + '.txt'

        f = open(day_path, "r")
        check = f.read().split('\n')
        f.close()
        check.remove(';'.join(p))
        f = open(day_path, "w")
        length = len(check)
        if length:
            f.write(check[0])
        for ii in range(1, length):
            f.write('\n'+check[ii])
        f.close()

        self.close()

    def show(self):
        QDialog.show(self)
        global p

        self.edit1.lineEdit_2.setText(p[0])
        date = p[1].split('/')
        time = p[2].split(':')
        date2 = p[3].split('/')
        time2 = p[4].split(':')
        self.edit1.dateTimeEdit.setDate(QtCore.QDate(int(date[0]), int(date[1]), int(date[2])))
        self.edit1.dateTimeEdit.setTime(QtCore.QTime(int(time[0]), int(time[1])))
        self.edit1.dateTimeEdit_2.setDate(QtCore.QDate(int(date2[0]), int(date2[1]), int(date2[2])))
        self.edit1.dateTimeEdit_2.setTime(QtCore.QTime(int(time2[0]), int(time2[1])))

        self.edit1.spinBox.setCurrentText(p[5])
        self.edit1.comboBox.setCurrentText(p[6])

        self.edit1.lineEdit.setText(p[7])
        x = int(p[8])
        if x == 0:
            self.edit1.radioButton.setChecked(True)
        elif x == 1:
            self.edit1.radioButton_2.setChecked(True)
        elif x == 2:
            self.edit1.radioButton_3.setChecked(True)
        else:
            self.edit1.radioButton_4.setChecked(True)

        if len(btn_add_e1):
            self.edit1.comboBox.addItems(btn_add_e1)
            btn_add_e1.clear()


class childWindow4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.routine = Ui_Dialog4()
        self.routine.setupUi(self)

        self.routine.buttonBox_2.accepted.connect(self.accept)
        self.routine.buttonBox_2.rejected.connect(self.reject)

    def accept(self):
        title = self.routine.lineEdit_2.text()
        start = self.routine.timeEdit.text()
        end = self.routine.timeEdit_2.text()
        if start>=end:  # TODO 起始时间大于结束时间 error1
            #global nowstr
            #nowstr = error1
            errorSymbol1.show()
            self.close()
            return


        start_time = start.split(":")
        importance = self.routine.spinBox.currentText()
        tag = self.routine.comboBox.currentText()
        attach = self.routine.lineEdit.text()

        l = [title, '', start, '', end, importance, tag, attach, str(0)]

        window.addRoutine(int(start_time[0])//2, start + " " + title, l)
        self.close()

    def show(self):
        if len(btn_add_4):
            self.routine.comboBox.addItems(btn_add_4)
            btn_add_4.clear()
        QDialog.show(self)


class editWindow4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.edit4 = Ui_Dialog44()
        self.edit4.setupUi(self)
        self.edit4.buttonBox_2.accepted.connect(self.accept)
        self.edit4.buttonBox_2.rejected.connect(self.rejectt)

    def accept(self):
        global pindex
        title = self.edit4.lineEdit_2.text()
        s = self.edit4.timeEdit.text()
        e = self.edit4.timeEdit_2.text()
        if s>=e:  # TODO 起始时间大于结束时间 error1
            #global nowstr
            #nowstr = error1
            errorSymbol1.show()
            self.close()
            return
        start_time = s.split(":")
        importance = self.edit4.spinBox.currentText()
        tag = self.edit4.comboBox.currentText()
        attach = self.edit4.lineEdit.text()

        state = 0

        if self.edit4.radioButton.isChecked():
            state = 0
        elif self.edit4.radioButton_2.isChecked():
            state = 1
        elif self.edit4.radioButton_3.isChecked():
            state = 2
        else:
            state = 3

        if s>=e:  #TODO 起始时间大于结束时间
            print("REEOR1")
            return
        # TODO0812日期一样

        # 存在txt，否则创建
        for datee in weekDate:

            year_path = desk_path + global_user.getName() + '/' + datee[0]
            month_path = year_path + '/' + datee[1]
            day_path = month_path + '/' + datee[2] + '.txt'
            if os.path.exists(year_path):  # 判断桌面是否存在输入的文件夹，存在则继续
                if os.path.exists(month_path):  # 判断否存在输入的子文件夹

                    if os.path.exists(day_path):
                        continue
                    f = open(day_path, 'w')
                    f.close()
                else:  # 桌面文件夹存在，子文件夹不存在，则创建
                    os.mkdir(month_path)  # 创建子文件夹
                    f = open(day_path, 'w')
                    f.close()
            else:  # 桌面文件夹不存在，则创建桌面文件夹和子文件夹
                os.mkdir(year_path)  # 创建桌面文件夹
                os.mkdir(month_path)
                f = open(day_path, 'w')
                f.close()

        r = int(start_time[0]) // 2
        l = [title, '', s, '', e, importance, tag, attach, str(0)]  # TODO 完成情况

        global global_col
        ddate = weekPath[global_col]

        global p

        #旧的有没有日期
        has_p = 0

        #新的list[//,0]
        new_list = []

        #旧的有list
        if len(p) == 10:
            t0 = p[9].split('.')
            for t in t0:

                t2 = t.split(',')
                if t2[0] == ddate:
                    new_list.append(ddate+','+str(state))
                    has_p = 1
                else:
                    new_list.append(t)
            if has_p == 0:
                new_list.append(ddate + ',' + str(state))

        else:
            new_list.append(ddate+','+str(state))

        l.append('.'.join(new_list))

        global global_row
        global dele_text
        window.deleRoutine(global_row, dele_text, p)
        window.addRoutine(r, s + ' ' + title, l)
        self.close()

    def rejectt(self):
        global pindex
        global global_row
        global global_col
        global p
        window.deleRoutine(global_row, dele_text, p)
        self.close()

    def show(self):
        QDialog.show(self)
        global p

        self.edit4.lineEdit_2.setText(p[0])

        time = p[2].split(':')

        time2 = p[4].split(':')

        self.edit4.timeEdit.setTime(QtCore.QTime(int(time[0]), int(time[1])))

        self.edit4.timeEdit_2.setTime(QtCore.QTime(int(time2[0]), int(time2[1])))

        self.edit4.spinBox.setCurrentText(p[5])
        self.edit4.comboBox.setCurrentText(p[6])

        self.edit4.lineEdit.setText(p[7])

        x = int(p[8])
        ###0812new
        global global_col
        ddate = weekPath[global_col]
        if len(p) == 10:
            t0 = p[9].split('.')
            for t in t0:
                t2 = t.split(',')
                if t2[0] == ddate:
                    x = int(t2[1])
        ###0812new
        if x == 0:
            self.edit4.radioButton.setChecked(True)
        elif x == 1:
            self.edit4.radioButton_2.setChecked(True)
        elif x == 2:
            self.edit4.radioButton_3.setChecked(True)
        else:
            self.edit4.radioButton_4.setChecked(True)

        if len(btn_add_e4):
            self.edit4.comboBox.addItems(btn_add_e4)
            btn_add_e4.clear()


class childWindow2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.free_create = Ui_Dialog2()
        self.free_create.setupUi(self)

        self.free_create.buttonBox_2.accepted.connect(self.accept)
        self.free_create.buttonBox_2.rejected.connect(self.reject)

    def show(self):
        if len(btn_add_2):
            self.free_create.comboBox.addItems(btn_add_2)
            btn_add_2.clear()
        QDialog.show(self)

    def accept(self):
        title = self.free_create.lineEdit_2.text()
        end = self.free_create.dateTimeEdit_2.text().split(" ")
        end_date = end[0]
        end_time = end[1]

        last_time = self.free_create.timeEdit.text()
        if last_time=='00:00':  # TODO 代办事项的持续时间不能为0 error3
            #global nowstr

            errorSymbol3.show()
            self.close()
            return
        importance = self.free_create.spinBox.currentText()
        tag = self.free_create.comboBox.currentText()
        attach = self.free_create.lineEdit.text()

        l = [title, '', last_time, end[0], end[1], importance, tag, attach, str(0)]

        split_list.append((end_date + " "+end_time, l))

        window.addToDo()  # TODO TODO1
        '''
        f = open(desk_path + global_user.getName()+'/'+'ToDo.txt', "a")
        if len(split_list):
            f.write('\n')
        f.write(';'.join(l))
        f.close()
        '''
        if last_time>='04:00':  # TODO 可能没有足够长的空闲 error5
            #global nowstr

            errorSymbol.show()
            self.close()
            return



        self.close()


class childWindow2_edit(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.edit3 = Ui_Dialog33()
        self.edit3.setupUi(self)
        self.edit3.buttonBox_2.accepted.connect(self.accept)
        self.edit3.buttonBox_2.rejected.connect(self.rejectt)

    def show(self):
        QDialog.show(self)
        global p

        self.edit3.lineEdit_2.setText(p[0])

        date = p[3].split('/')
        time = p[4].split(':')
        self.edit3.dateTimeEdit_2.setDate(QtCore.QDate(int(date[0]), int(date[1]), int(date[2])))
        self.edit3.dateTimeEdit_2.setTime(QtCore.QTime(int(time[0]), int(time[1])))

        last_time = p[2].split(':')
        self.edit3.timeEdit.setTime(QtCore.QTime(int(last_time[0]),int(last_time[1])))

        self.edit3.spinBox.setCurrentText(p[5])
        self.edit3.comboBox.setCurrentText(p[6])
        self.edit3.lineEdit.setText(p[7])

        x = int(p[8])
        if x == 0:
            self.edit3.radioButton.setChecked(True)
        elif x == 1:
            self.edit3.radioButton_2.setChecked(True)
        elif x == 2:
            self.edit3.radioButton_3.setChecked(True)
        else:
            self.edit3.radioButton_4.setChecked(True)

        if len(btn_add_3):
            self.edit3.comboBox.addItems(btn_add_3)
            btn_add_3.clear()

    def accept(self):
        global pindex
        title = self.edit3.lineEdit_2.text()
        end = self.edit3.dateTimeEdit_2.text().split(" ")
        end_date = end[0]
        end_time = end[1]
        last_time = self.edit3.timeEdit.text()
        if last_time=='00:00':  # TODO 代办事项的持续时间不能为0 error3
            #global nowstr

            errorSymbol3.show()
            self.close()
            return
        importance = self.edit3.spinBox.currentText()
        tag = self.edit3.comboBox.currentText()
        attach = self.edit3.lineEdit.text()

        state = 0
        if self.edit3.radioButton.isChecked():
            state = 0
        elif self.edit3.radioButton_2.isChecked():
            state = 1
        elif self.edit3.radioButton_3.isChecked():
            state = 2
        else:
            state = 3

        if state==2:
            global pindex
            global p

            split_list.pop(pindex)

            ### 全局变量删除 主视图更新
            window.addToDo()

            f = open(desk_path + global_user.getName() + '/' + 'ToDo.txt', "w")
            if len(split_list):
                f.write(';'.join(split_list[0][1]))
                for i in range(1, len(split_list)):
                    f.write('\n')
                    f.write(';'.join(split_list[i][1]))
            f.close()
            errorSymbol7.show()#####error7 todo 完成，删除
            self.close()
            return



        l = [title, '', last_time, end[0], end[1], importance, tag, attach, str(state)]

        split_list[pindex] = (end_date + " " + end_time, l)

        window.addToDo()
        '''
        f = open(desk_path + global_user.getName()+'/'+'ToDo.txt', "w")
        f.write(';'.join(split_list[0][1]))
        for i in range(1,len(split_list)):
            f.write('\n')
            f.write(';'.join(split_list[i][1]))
        f.close()
        '''
        if last_time>='04:00':  # TODO 可能没有足够长的空闲 error5
            #global nowstr

            errorSymbol.show()
            self.close()
            return

        self.close()

    def rejectt(self):
        global pindex
        global p

        split_list.pop(pindex)

        ### 全局变量删除 主视图更新
        window.addToDo()

        f = open(desk_path + global_user.getName() + '/' + 'ToDo.txt', "w")
        if len(split_list):
            f.write(';'.join(split_list[0][1]))
            for i in range(1, len(split_list)):
                f.write('\n')
                f.write(';'.join(split_list[i][1]))
        f.close()

        self.close()

class errorWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error = Ui_Dialoge()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error.setupUi(self)

class errorWindow1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error1 = Ui_Dialoge1()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error1.setupUi(self)

class errorWindow2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error2 = Ui_Dialoge2()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error2.setupUi(self)

class errorWindow3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error3 = Ui_Dialoge3()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error3.setupUi(self)

class errorWindow4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error4 = Ui_Dialoge4()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error4.setupUi(self)

class errorWindow6(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error6 = Ui_Dialoge6()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error6.setupUi(self)


class errorWindow7(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.error7 = Ui_Dialoge7()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.error7.setupUi(self)

class childWindow3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.new_tag = Ui_Dialog3()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.new_tag.setupUi(self)

        self.new_tag.buttonBox.accepted.connect(self.accept)
        self.new_tag.buttonBox.rejected.connect(self.reject)

    def accept(self):

        newstr = self.new_tag.lineEdit.text()
        f = open(desk_path + global_user.getName() + '/' + "tags.txt", "r")
        t = f.read().split("\n")
        f.close()
        if newstr in t:
            self.close()
            return
        if len(t) == 8:
            #error6
            if s >= e:  # TODO 太多了 error6
                # global nowstr
                # nowstr = error1
                errorSymbol6.show()
                self.close()
                return

            self.close()
            return

        f = open(desk_path + global_user.getName()+'/'+"tags.txt", "a")

        f.write("\n"+newstr)
        btn_add_1.append(newstr)
        btn_add_2.append(newstr)
        btn_add_3.append(newstr)
        btn_add_4.append(newstr)
        btn_add_e1.append(newstr)
        btn_add_e4.append(newstr)

        self.close()


app = QApplication(sys.argv)
window = parentWindow()
child = childWindow()
child2 = childWindow2()
child3 = childWindow3()
child4 = childWindow4()

errorSymbol=errorWindow()
errorSymbol1=errorWindow1()
errorSymbol2=errorWindow2()
errorSymbol3=errorWindow3()
errorSymbol4=errorWindow4()
errorSymbol6=errorWindow6()
errorSymbol7=errorWindow7()

child1_edit = editWindow1()
child2_edit = childWindow2_edit()
child4_edit = editWindow4()

child5=distriWindow()


btn = window.main_view.pushButton
btn.clicked.connect(child.show)

btn2 = window.main_view.pushButton_2
btn2.clicked.connect(child2.show)

btn3 = window.main_view.pushButton_3
btn3.clicked.connect(child3.show)

btn4 = window.main_view.pushButton_4
btn4.clicked.connect(child4.show)

btn5 = window.main_view.pushButton_5
btn5.clicked.connect(child5.show)


#btn5.clicked.connect(window.change())

tableItem = window.main_view.tableWidget
tableItem.cellClicked.connect(window.cfgItemShowed)


listItem = window.main_view.listWidget
listItem_2 = window.main_view.listWidget_2

listItem.itemClicked.connect(window.itemShowedx)
listItem_2.itemClicked.connect(window.toDoItemShowedx)
