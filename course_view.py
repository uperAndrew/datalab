# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course_view.ui'
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
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 260, 351, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 30, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 130, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ID = QtWidgets.QLabel(Form)
        self.ID.setGeometry(QtCore.QRect(310, 90, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ID.setFont(font)
        self.ID.setObjectName("ID")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(310, 130, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(400, 260, 361, 251))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.goback = QtWidgets.QPushButton(Form)
        self.goback.setGeometry(QtCore.QRect(520, 180, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Course"))
        self.label_2.setText(_translate("Form", "ID："))
        self.label_3.setText(_translate("Form", "Name:"))
        self.ID.setText(_translate("Form", "TextLabel"))
        self.Name.setText(_translate("Form", "TextLabel"))
        self.goback.setText(_translate("Form", "返回上一层"))
