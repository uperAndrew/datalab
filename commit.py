# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commit.ui'
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 160, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 280, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sex = QtWidgets.QComboBox(Form)
        self.sex.setGeometry(QtCore.QRect(250, 220, 67, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.sex.addItem("")
        self.sfz = QtWidgets.QLineEdit(Form)
        self.sfz.setGeometry(QtCore.QRect(250, 160, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sfz.setFont(font)
        self.sfz.setObjectName("sfz")
        self.birth = QtWidgets.QLineEdit(Form)
        self.birth.setGeometry(QtCore.QRect(250, 280, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.birth.setFont(font)
        self.birth.setObjectName("birth")
        self.commit = QtWidgets.QPushButton(Form)
        self.commit.setGeometry(QtCore.QRect(140, 390, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commit.setFont(font)
        self.commit.setObjectName("commit")
        self.goback = QtWidgets.QPushButton(Form)
        self.goback.setGeometry(QtCore.QRect(380, 390, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 340, 54, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.major = QtWidgets.QLineEdit(Form)
        self.major.setGeometry(QtCore.QRect(250, 340, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.major.setFont(font)
        self.major.setObjectName("major")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "身份证号："))
        self.label_3.setText(_translate("Form", "性别："))
        self.label_4.setText(_translate("Form", "出生日期："))
        self.sex.setItemText(0, _translate("Form", "男"))
        self.sex.setItemText(1, _translate("Form", "女"))
        self.sex.setItemText(2, _translate("Form", "未知"))
        self.commit.setText(_translate("Form", "注册档案"))
        self.goback.setText(_translate("Form", "返回上一层"))
        self.label.setText(_translate("Form", "专业："))
