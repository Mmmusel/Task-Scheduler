from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 441)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 30, 235, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFixedSize(235, 30)
        self.lineEdit_2.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setFixedSize(235, 30)
        self.dateTimeEdit.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_2.setFixedSize(235, 30)
        self.dateTimeEdit_2.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.dateTimeEdit_2)
        self.spinBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setFixedSize(235, 30)
        self.spinBox.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.spinBox)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFixedSize(235, 30)
        self.comboBox.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.comboBox)
        #fun.tran(self)
        self.spinBox.addItems(["", "", "", "", ""])
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFixedSize(235, 30)
        self.lineEdit.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.verticalLayout.addWidget(self.lineEdit)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.verticalLayout.addWidget(self.buttonBox_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 40, 110, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.verticalLayout_2.addWidget(self.label_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "??????????????????"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd HH:mm"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd HH:mm"))
        #fun.retran(self)
        for i in range(0, 5):
            self.spinBox.setItemText(i, _translate("Dialog", str(5 - i)))
        self.label.setText(_translate("Dialog", "?????????"))
        self.label_3.setText(_translate("Dialog", "???????????????"))
        self.label_5.setText(_translate("Dialog", "???????????????"))
        self.label_4.setText(_translate("Dialog", "????????????"))
        self.label_2.setText(_translate("Dialog", "?????????"))
        self.label_6.setText(_translate("Dialog", "?????????"))
