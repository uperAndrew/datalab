# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'award.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 170, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(220, 170, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.ID = QtWidgets.QLabel(Form)
        self.ID.setGeometry(QtCore.QRect(220, 220, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ID.setFont(font)
        self.ID.setObjectName("ID")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 220, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(330, 110, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.goback = QtWidgets.QPushButton(Form)
        self.goback.setGeometry(QtCore.QRect(530, 530, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(110, 270, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Sum = QtWidgets.QLabel(Form)
        self.Sum.setGeometry(QtCore.QRect(220, 270, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Sum.setFont(font)
        self.Sum.setObjectName("Sum")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 320, 331, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name:"))
        self.Name.setText(_translate("Form", "Name"))
        self.ID.setText(_translate("Form", "ID"))
        self.label_4.setText(_translate("Form", "IDNumber:"))
        self.label_5.setText(_translate("Form", "奖惩情况汇总"))
        self.goback.setText(_translate("Form", "返回上一层"))
        self.label_6.setText(_translate("Form", "Sum:"))
        self.Sum.setText(_translate("Form", "Sum"))