import os

from PyQt5 import QtCore, QtGui, QtWidgets

import global_user


class Ui_Form(object):
    def setupUi(self, Form, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(220, 400)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 73, 400))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 10, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 40, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.TodoLabel = []
        self.TodoTextEdit = []
        self.showTodo(Form)
        self.pushButton.clicked.connect(lambda: self.edit())
        self.pushButton_2.clicked.connect(lambda: self.save())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Details"))
        self.pushButton.setText(_translate("Form", "编辑"))
        self.pushButton_2.setText(_translate("Form", "确认修改"))

    def get_todo(self, path):
        todos = []
        if not os.path.exists(path):
            return todos
        f = open(str(path))
        lines = f.readlines()
        for line in lines:
            items = line.split(';')
            #####################################没处理任务不在同一天内
            starth = items[2].split(':')[1]
            startm = items[2].split(':')[2]
            endh = items[3].split(':')[1]
            endm = items[3].split(':')[2]
            todos.append([items[0], items[1], starth, startm, endh, endm, items[4]])
        return todos

    def getTodos(self):
        # 这个 mpath应该是一个全局变量   在登陆后 设置为对应的用户所处的文件夹位置
        path = "data" + '\\' + global_user.getName() + '\\' + str(self.year) + '\\' + str(self.month) + '\\' + str(self.day) + '.txt'
        self.todo = self.get_todo(path)

    def edit(self):
        for testedit in self.TodoTextEdit:
            testedit.setReadOnly(False)

    def showTodo(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.getTodos()
        for t in self.todo:  #没有添加    如果时间比较短就不显示文字    的功能
            tmp = QtWidgets.QLabel(Form)
            h1 = (int(t[2])*60 + int(t[3]))/1440*400
            h2 = (int(t[4])*60 + int(t[5]))/1440*400
            tmp.setGeometry(QtCore.QRect(1, int(h1), 70, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            tmp.setFont(font)
            tmp.setLineWidth(0)
            tmp.setScaledContents(False)
            tmp.setAlignment(QtCore.Qt.AlignCenter)
            tmp.setWordWrap(False)
            tmp.setIndent(0)
            tmp.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
            tmp.setObjectName("label")
            tmp.setText(_translate("Form", t[0]))
            self.TodoLabel.append(tmp)
            tmpplainTextEdit = QtWidgets.QPlainTextEdit(Form)
            tmpplainTextEdit.setGeometry(QtCore.QRect(1, int(h1) + 16, 70, int(h2 - h1) - 16))
            tmpplainTextEdit.setStyleSheet("background:rgb(255, 52, 16)")
            tmpplainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
            tmpplainTextEdit.setUndoRedoEnabled(True)
            tmpplainTextEdit.setReadOnly(True)
            tmpplainTextEdit.setObjectName("plainTextEdit_2")
            tmpplainTextEdit.setPlainText(_translate("Form", t[1]))
            imp = int(t[6])
            if imp == 0:
                tmp.setStyleSheet("background:rgba(251, 255, 179, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(251, 255, 179, 255)\n""")
            elif imp == 1:
                tmp.setStyleSheet("background:rgba(255, 239, 60, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(255, 239, 60, 255)\n""")
            elif imp == 2:
                tmp.setStyleSheet("background:rgba(255, 21, 52, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(255, 21, 52, 255)\n""")
            elif imp == 3:
                tmp.setStyleSheet("background:rgba(255, 176, 39, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(255, 176, 39, 255)\n""")
            elif imp == 4:
                tmp.setStyleSheet("background:rgba(255, 108, 23, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(255, 108, 23, 255)\n""")
            elif imp == 5:
                tmp.setStyleSheet("background:rgba(255, 64, 16, 255)\n""")
                tmpplainTextEdit.setStyleSheet("background:rgba(255, 64, 16, 255)\n""")
            self.TodoTextEdit.append(tmpplainTextEdit)
