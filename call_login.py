import sys
import pymysql
import os
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
# 导入designer工具生成的login模块
from login import Ui_Form as loginForm
from main import Ui_Form as mainForm
from award import Ui_Form as awardForm
from course import Ui_Form as courseForm
from commit import Ui_Form as commitForm
from course_view import Ui_Form as courseviewForm
from error import Ui_Form as errorForm
from PyQt5 import QtCore

class MyLoginForm(QMainWindow, loginForm):
    def __init__(self, parent=None):
        super(MyLoginForm, self).__init__(parent)
        self.setupUi(self)
    def reset(self):
        self.NameEdit.clear()
        self.IDEdit.clear()
class MyMainForm(QMainWindow, mainForm):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

class MyAwardForm(QMainWindow, awardForm):
    def __init__(self, parent=None):
        super(MyAwardForm, self).__init__(parent)
        self.setupUi(self)

class MyCourseForm(QMainWindow, courseForm):
    def __init__(self, parent=None):
        super(MyCourseForm, self).__init__(parent)
        self.setupUi(self)

class MyCommitForm(QMainWindow, commitForm):
    def __init__(self, parent=None):
        super(MyCommitForm, self).__init__(parent)
        self.setupUi(self)

class MyCourseviewForm(QMainWindow, courseviewForm):
    def __init__(self, parent=None):
        super(MyCourseviewForm, self).__init__(parent)
        self.setupUi(self)
class MyErrorForm(QMainWindow, errorForm):
    def __init__(self, parent=None):
        super(MyErrorForm, self).__init__(parent)
        self.setupUi(self)

class MySql():
    def __init__(self):
        self.connection=pymysql.connect(host='localhost',
                                        user='root',
                                        password='mtr20040629',
                                        db='datalab',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)

    def execute_query(self,sql_query):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()
    def login(self,id,name):
        if(len(id)==0 or len(name)==0):
            print("error")
            Error.show()
            return
        sql_query=f"select * from stu where stu.id='{id}' and stu.name='{name}'"
        result=self.execute_query(sql_query)
        if(len(result)==0):
            print("error")
            Error.show()
            return
        self.id=id
        self.name=name
        myCommit.sfz.clear()
        myCommit.birth.clear()
        myCommit.major.clear()
        myMain.show()
        myLogin.close()
    def commit(self,id,name,sfz,sex,birth,major):
        if(len(sfz)==0 or len(sex)==0 or len(birth)==0 or len(major)==0):
            print("error")
            Error.show()
            return
        sql_query=f"select * from stu where stu.id='{id}'"
        result=self.execute_query(sql_query)
        if(len(result)!=0):
            print("注册失败！")
        else:
            sql_query=f"insert into stu values('{id}','{name}','{major}','doc/{id}.txt',0)"
            self.execute_query(sql_query)
            self.connection.commit()
            with open(f"doc/{id}.txt",'w',encoding='utf-8')as file:
                print(f"id={id}",file=file)
                print(f"name={name}",file=file)
                print(f"sfz={sfz}",file=file)
                print(f"sex={sex}",file=file)
                print(f"birth={birth}",file=file)
                print(f"major={major}",file=file)
    def open_commit(self,id,name):
        if(len(id)==0 or len(name)==0):
            print("error")
            Error.show()
            return
        sql_query=f"select doc from stu where stu.id='{id}' and stu.name='{name}'"
        result=self.execute_query(sql_query)
        os.system(f"notepad {result[0]['doc']}")

    def majorEdit(self,majorName):
        if(len(majorName)==0):
            print("error")
            Error.show()
            return
        sql_query=f"select * from stu where stu.id='{self.id}'"
        result=self.execute_query(sql_query)
        with open(f"{result[0]['doc']}",'a',encoding='utf-8')as file:
            print(f"new major={majorName}",file=file)
        sql_query = f"update stu set major='{majorName}' where stu.id='{self.id}'"
        self.execute_query(sql_query)
        self.connection.commit()

    def awardEdit(self,awardtype,awardtime,awardname):
        if(len(awardtype)==0 or len(awardname)==0 or len(awardtime)==0):
            print("error")
            Error.show()
            return
        sql_query=f"insert into award values('{self.id}','{awardtype}','{awardtime}','{awardname}')"
        self.execute_query(sql_query)
        self.connection.commit()
    def awardDelete(self,awardtype,awardtime,awardname):
        if (len(awardtype) == 0 or len(awardname) == 0 or len(awardtime) == 0):
            print("error")
            Error.show()
            return
        sql_query=(f"delete from award where award.id='{self.id}' and award.award='{awardtype}'\
                   and award.award_time='{awardtime}'and award.award_name='{awardname}'")
        self.execute_query(sql_query)
        self.connection.commit()
    def awardSearch(self):
        myAward.Name.setText(f"{self.name}")
        myAward.ID.setText(f"{self.id}")
        sql_query=f"select award_times from stu where id='{self.id}'"
        result=self.execute_query(sql_query)
        myAward.Sum.setText(f"{result[0]['award_times']}")
        sql_query = f"select * from award where id='{self.id}'"
        result = self.execute_query(sql_query)
        if(len(result)==0):
            return
        myAward.tableWidget.setRowCount(len(result))
        myAward.tableWidget.setColumnCount(3)
        myAward.tableWidget.setHorizontalHeaderLabels(['award_type', 'award_time', 'award_name'])
        for i in range(len(result)):
            item = QTableWidgetItem(result[i]['award'])
            myAward.tableWidget.setItem(i,0,item)
            item = QTableWidgetItem(str(result[i]['award_time']))
            myAward.tableWidget.setItem(i,1,item)
            item = QTableWidgetItem(result[i]['award_name'])
            myAward.tableWidget.setItem(i,2,item)
    def sel_course(self,num,name,cred):
        if(len(num)==0 or len(name)==0 or len(cred)==0):
            print("error")
            Error.show()
            return
        sql_query=f"insert into course values('{self.id}','{num}','{name}',{cred},'false')"
        self.execute_query(sql_query)
        self.connection.commit()
    def del_course(self,num,name):
        if(len(num)==0 or len(name)==0):
            print("error")
            Error.show()
            return
        sql_query=f"select * from course where id='{self.id}' and course_num='{num}'\
                   and course_name='{name}' and have_grade='false'"
        result=self.execute_query(sql_query)
        if(len(result)==0):
            print("error")
            Error.show()
            return
        sql_query=f"delete from course where id='{self.id}' and course_num='{num}'\
                   and course_name='{name}' and have_grade='false'"
        self.execute_query(sql_query)
        self.connection.commit()
    def commit_course(self,num,name,grade):
        if(len(num)==0 or len(name)==0 or len(grade)==0):
            print("error")
            Error.show()
            return
        with self.connection.cursor() as cursor:
            result=cursor.callproc('commit_grade',args=[self.id,num,name,int(grade)])
            self.connection.commit()
    def calc_gpa(self):
        sql_query=f"select gpa('{self.id}')"
        result=self.execute_query(sql_query)
        myCourse.GPA.setText(str(result[0][f"gpa('{self.id}')"]))
    def ListC(self):
        myCourseview.ID.setText(f"{self.id}")
        myCourseview.Name.setText(f"{self.name}")
        sql_query=f"select * from course where course.id='{self.id}'"
        result=self.execute_query(sql_query)
        if (len(result) == 0):
            return
        myCourseview.tableWidget.setRowCount(len(result))
        myCourseview.tableWidget.setColumnCount(4)
        myCourseview.tableWidget.setHorizontalHeaderLabels(['c_num','c_name','cred','have_grade'])
        for i in range(len(result)):
            item = QTableWidgetItem(result[i]['course_num'])
            myCourseview.tableWidget.setItem(i, 0, item)
            item = QTableWidgetItem(result[i]['course_name'])
            myCourseview.tableWidget.setItem(i, 1, item)
            item = QTableWidgetItem(str(result[i]['cred']))
            myCourseview.tableWidget.setItem(i, 2, item)
            item = QTableWidgetItem(result[i]['have_grade'])
            myCourseview.tableWidget.setItem(i, 3, item)
        sql_query = f"select * from course_grade where id='{self.id}'"
        result = self.execute_query(sql_query)
        if (len(result) == 0):
            return
        myCourseview.tableWidget_2.setRowCount(len(result))
        myCourseview.tableWidget_2.setColumnCount(4)
        myCourseview.tableWidget_2.setHorizontalHeaderLabels(['c_num', 'c_name', 'cred', 'grade'])
        for i in range(len(result)):
            item = QTableWidgetItem(result[i]['course_num'])
            myCourseview.tableWidget_2.setItem(i, 0, item)
            item = QTableWidgetItem(result[i]['course_name'])
            myCourseview.tableWidget_2.setItem(i, 1, item)
            item = QTableWidgetItem(str(result[i]['cred']))
            myCourseview.tableWidget_2.setItem(i, 2, item)
            item = QTableWidgetItem(str(result[i]['grade']))
            myCourseview.tableWidget_2.setItem(i, 3, item)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 初始化
    myLogin = MyLoginForm()
    myMain = MyMainForm()
    myAward = MyAwardForm()
    myCourse = MyCourseForm()
    myCommit = MyCommitForm()
    Error=MyErrorForm()
    mySql = MySql()
    myCourseview=MyCourseviewForm()
    # 将窗口控件显示在屏幕上
    myLogin.show()
    myLogin.login.clicked.connect(lambda:mySql.login(myLogin.IDEdit.text(),myLogin.NameEdit.text()))
    myLogin.commit.clicked.connect(myLogin.close)
    myLogin.commit.clicked.connect(myCommit.show)
    myLogin.pushButton_2.clicked.connect(lambda :mySql.open_commit(myLogin.IDEdit.text(),myLogin.NameEdit.text()))
    myMain.pushButton.clicked.connect(myMain.close)
    myMain.pushButton.clicked.connect(myLogin.show)
    myMain.pushButton.clicked.connect(myLogin.reset)
    myMain.awardSearch.clicked.connect(myAward.show)
    myMain.awardSearch.clicked.connect(myMain.close)
    myMain.majorEdit.clicked.connect(lambda:mySql.majorEdit(myMain.majorName.text()))
    myMain.awardEdit.clicked.connect(lambda:mySql.awardEdit(myMain.awardType.currentText(),myMain.awardTime.text()\
                                                            ,myMain.awardName.text()))
    myMain.awardDelete.clicked.connect(lambda:mySql.awardDelete(myMain.awardType.currentText(),myMain.awardTime.text()\
                                                            ,myMain.awardName.text()))
    myMain.awardSearch.clicked.connect(lambda :mySql.awardSearch())
    myCourse.goback.clicked.connect(myMain.show)
    myCourse.goback.clicked.connect(myCourse.close)
    myCommit.goback.clicked.connect(myLogin.show)
    myCommit.goback.clicked.connect(myCommit.close)
    myCommit.goback.clicked.connect(myLogin.reset)
    myCommit.commit.clicked.connect(lambda :mySql.commit(myLogin.IDEdit.text(),myLogin.NameEdit.text(),\
                    myCommit.sfz.text(),myCommit.sex.currentText(),myCommit.birth.text(),myCommit.major.text()))
    myMain.Course.clicked.connect(myMain.close)
    myMain.Course.clicked.connect(myCourse.show)
    myAward.goback.clicked.connect(myAward.close)
    myAward.goback.clicked.connect(myMain.show)
    myCourse.Sel.clicked.connect(lambda :mySql.sel_course(myCourse.CourseNumber.text(),myCourse.CourseName.text(),myCourse.CourseCred.text()))
    myCourse.Del.clicked.connect(
        lambda: mySql.del_course(myCourse.CourseNumber.text(), myCourse.CourseName.text()))
    myCourse.commit.clicked.connect(
        lambda: mySql.commit_course(myCourse.CourseNumber.text(), myCourse.CourseName.text(),myCourse.CourseGrade.text()))
    myCourse.GPAquery.clicked.connect(lambda:mySql.calc_gpa())
    myCourse.List.clicked.connect(lambda :mySql.ListC())
    myCourse.List.clicked.connect(myCourse.close)
    myCourse.List.clicked.connect(myCourseview.show)
    myCourseview.goback.clicked.connect(myCourse.show)
    myCourseview.goback.clicked.connect(myCourseview.close)
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())