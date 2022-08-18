import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from var import desk_path
import global_user


def tran(self):
    f = open(desk_path+global_user.getName()+"tags.txt", "r")
    self.comboBox.addItems((f.read().split('\n')))
    f.close()
    self.spinBox.addItems(["","","","",""])


def retran(self):
    f = open(desk_path+global_user.getName()+"tags.txt", "r")
    x = ((f.read().split('\n')))
    for i in range(0, len(x)):
        self.comboBox.setItemText(i, PyQt5.QtCore.QCoreApplication.translate("Dialog", x[i]))
    f.close()
    for i in range(0, 5):
        self.spinBox.setItemText(i, PyQt5.QtCore.QCoreApplication.translate("Dialog", str(5 - i)))

