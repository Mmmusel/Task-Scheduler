from PyQt5 import QtCore, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 100, 30))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 25 10pt \"Microsoft YaHei\";                 \n"
                                 "border-radius: 4px;                                             \n"
                                 "color: rgb(255, 255, 255);        \n"
                                 "background-color: rgb(198, 198, 198);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(185, 90, 141, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFixedSize(141, 30)
        self.lineEdit.setStyleSheet('border:2px solid rgb(186,186,186);border-radius:10px')
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 140, 233, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新建事项分类"))
        self.label.setText(_translate("Dialog", "新建标签:"))
