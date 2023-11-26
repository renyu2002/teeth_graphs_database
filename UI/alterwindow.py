# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alterwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget
import pymysql
import os


class Ui_Alter(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1237, 1035)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(370, 10, 641, 81))
        self.title.setStyleSheet("font: 48pt  \"微软雅黑\";")
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 100, 451, 71))
        self.widget.setObjectName("widget")
        self.namesearch_label = QtWidgets.QLabel(self.widget)
        self.namesearch_label.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.namesearch_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.namesearch_label.setObjectName("namesearch_label")
        self.namesearch_textEdit = QtWidgets.QTextEdit(self.widget)
        self.namesearch_textEdit.setGeometry(QtCore.QRect(190, 10, 241, 51))
        self.namesearch_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.namesearch_textEdit.setObjectName("namesearch_textEdit")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(660, 100, 451, 71))
        self.widget_2.setObjectName("widget_2")
        self.IDsearch_label = QtWidgets.QLabel(self.widget_2)
        self.IDsearch_label.setGeometry(QtCore.QRect(20, 10, 141, 51))
        self.IDsearch_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.IDsearch_label.setObjectName("IDsearch_label")
        self.IDsearch_textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.IDsearch_textEdit.setGeometry(QtCore.QRect(170, 10, 261, 51))
        self.IDsearch_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.IDsearch_textEdit.setObjectName("IDsearch_textEdit")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(60, 190, 451, 80))
        self.widget_3.setObjectName("widget_3")
        self.namealter_label = QtWidgets.QLabel(self.widget_3)
        self.namealter_label.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.namealter_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.namealter_label.setObjectName("namealter_label")
        self.namealter_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.namealter_textEdit.setGeometry(QtCore.QRect(190, 10, 241, 51))
        self.namealter_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.namealter_textEdit.setObjectName("namealter_textEdit")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(60, 280, 451, 80))
        self.widget_4.setObjectName("widget_4")
        self.genderalter_label = QtWidgets.QLabel(self.widget_4)
        self.genderalter_label.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.genderalter_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.genderalter_label.setObjectName("genderalter_label")
        self.manalter_radioButton = QtWidgets.QRadioButton(self.widget_4)
        self.manalter_radioButton.setGeometry(QtCore.QRect(220, 10, 115, 19))
        self.manalter_radioButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.manalter_radioButton.setObjectName("manalter_radioButton")
        self.womanalter_radioButton = QtWidgets.QRadioButton(self.widget_4)
        self.womanalter_radioButton.setGeometry(QtCore.QRect(220, 50, 115, 19))
        self.womanalter_radioButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.womanalter_radioButton.setObjectName("womanalter_radioButton")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(60, 370, 451, 80))
        self.widget_5.setObjectName("widget_5")
        self.agealter_label = QtWidgets.QLabel(self.widget_5)
        self.agealter_label.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.agealter_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.agealter_label.setObjectName("agealter_label")
        self.agealter_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.agealter_doubleSpinBox.setGeometry(QtCore.QRect(210, 20, 201, 41))
        self.agealter_doubleSpinBox.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.agealter_doubleSpinBox.setObjectName("agealter_doubleSpinBox")
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(60, 640, 451, 191))
        self.widget_6.setObjectName("widget_6")
        self.locationalter_label = QtWidgets.QLabel(self.widget_6)
        self.locationalter_label.setGeometry(QtCore.QRect(10, 0, 401, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.locationalter_label.setFont(font)
        self.locationalter_label.setStyleSheet("")
        self.locationalter_label.setObjectName("locationalter_label")
        self.locationalter_textEdit = QtWidgets.QTextEdit(self.widget_6)
        self.locationalter_textEdit.setGeometry(QtCore.QRect(0, 70, 441, 51))
        self.locationalter_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.locationalter_textEdit.setObjectName("locationalter_textEdit")
        self.locationalter_pushButton = QtWidgets.QPushButton(self.widget_6)
        self.locationalter_pushButton.setGeometry(QtCore.QRect(120, 140, 181, 41))
        self.locationalter_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.locationalter_pushButton.setObjectName("locationalter_pushButton")
        self.locationalter_pushButton.clicked.connect(self.locate)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 160, 1231, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.result_textBrowser = QtWidgets.QTextBrowser(Form)
        self.result_textBrowser.setGeometry(QtCore.QRect(620, 200, 581, 701))
        self.result_textBrowser.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.alter_pushButton = QtWidgets.QPushButton(Form)
        self.alter_pushButton.setGeometry(QtCore.QRect(620, 940, 291, 41))
        self.alter_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.alter_pushButton.setObjectName("alter_pushButton")
        self.alter_pushButton.clicked.connect(self.alter)
        self.return_pushButton = QtWidgets.QPushButton(Form)
        self.return_pushButton.setGeometry(QtCore.QRect(920, 940, 291, 41))
        self.return_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.return_pushButton.setObjectName("return_pushButton")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(563, 170, 20, 861))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget_7 = QtWidgets.QWidget(Form)
        self.widget_7.setGeometry(QtCore.QRect(60, 460, 451, 80))
        self.widget_7.setObjectName("widget_7")
        self.nationalter_label = QtWidgets.QLabel(self.widget_7)
        self.nationalter_label.setGeometry(QtCore.QRect(0, 10, 201, 41))
        self.nationalter_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.nationalter_label.setObjectName("nationalter_label")
        self.nationalter_textEdit = QtWidgets.QTextEdit(self.widget_7)
        self.nationalter_textEdit.setGeometry(QtCore.QRect(190, 10, 241, 51))
        self.nationalter_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.nationalter_textEdit.setObjectName("nationalter_textEdit")
        self.widget_8 = QtWidgets.QWidget(Form)
        self.widget_8.setGeometry(QtCore.QRect(60, 550, 451, 80))
        self.widget_8.setObjectName("widget_8")
        self.positionnalter_label = QtWidgets.QLabel(self.widget_8)
        self.positionnalter_label.setGeometry(QtCore.QRect(10, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.positionnalter_label.setFont(font)
        self.positionnalter_label.setStyleSheet("")
        self.positionnalter_label.setObjectName("positionnalter_label")
        self.positionalter_textEdit = QtWidgets.QTextEdit(self.widget_8)
        self.positionalter_textEdit.setGeometry(QtCore.QRect(190, 10, 241, 51))
        self.positionalter_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.positionalter_textEdit.setObjectName("positionalter_textEdit")
        self.widget_9 = QtWidgets.QWidget(Form)
        self.widget_9.setGeometry(QtCore.QRect(60, 840, 511, 181))
        self.widget_9.setObjectName("widget_9")
        self.kindalter_label = QtWidgets.QLabel(self.widget_9)
        self.kindalter_label.setGeometry(QtCore.QRect(0, 60, 351, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kindalter_label.setFont(font)
        self.kindalter_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.kindalter_label.setObjectName("kindalter_label")
        self.kindalter_radioButton_1 = QtWidgets.QRadioButton(self.widget_9)
        self.kindalter_radioButton_1.setGeometry(QtCore.QRect(340, 20, 141, 31))
        self.kindalter_radioButton_1.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kindalter_radioButton_1.setObjectName("kindalter_radioButton_1")
        self.kindalter_radioButton_2 = QtWidgets.QRadioButton(self.widget_9)
        self.kindalter_radioButton_2.setGeometry(QtCore.QRect(340, 80, 141, 31))
        self.kindalter_radioButton_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kindalter_radioButton_2.setObjectName("kindalter_radioButton_2")
        self.kindalter_radioButton_3 = QtWidgets.QRadioButton(self.widget_9)
        self.kindalter_radioButton_3.setGeometry(QtCore.QRect(340, 130, 141, 31))
        self.kindalter_radioButton_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kindalter_radioButton_3.setObjectName("kindalter_radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def locate(self):
        location = QtWidgets.QFileDialog.getOpenFileName(None, "选取图片", "C:/")  # 起始路径
        location = str(location)
        location = location.replace('(','')
        location = location.replace(')','')
        location = location.replace(',','')
        location = location.replace("'",'')
        location = location.replace('All Files *','')
        location = location.strip()
        self.locationalter_textEdit.setText(location)

    def alter(self):

        if os.path.isfile('../bin/settings.txt'):
            f = open('../bin/settings.txt', 'r')
            settings = f.readlines()
            host = settings[0].strip()
            port = int(settings[1].replace('\n', ''))
            user = settings[2].replace('\n', '')
            pswd = settings[3].replace('\n', '')
            db_name = settings[4].replace('\n', '')
            table = settings[5].replace('\n', '')
        else:
            self.result_textBrowser.setText("数据库错误")

        # 打开数据库连接
        try:
            db = pymysql.connect(host=host, user=user, passwd=pswd, port=port, db=db_name)
            print('连接成功！')
        except:
            print('something wrong!')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql = "SELECT * FROM "+table+" WHERE name = '" + self.namesearch_textEdit.toPlainText() + "' OR id = '" + self.IDsearch_textEdit.toPlainText() +"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            namealter = row[2]
            genderalter = row[3]
            agealter = str(row[4])
            nationalter = row[5]
            positionalter = row[6]
            locationalter = row[7]
            kindalter = row[8]
        print(results)

        if (self.namealter_textEdit.toPlainText() != ''):
            namealter = self.namealter_textEdit.toPlainText()
        else:
            namealter =namealter
        print(namealter)
        if (self.manalter_radioButton.isChecked() == True):
            genderalter = '男'
        elif(self.womanalter_radioButton.isChecked() == True):
            genderalter = '女'
        else:
            genderalter = genderalter
        print(genderalter)
        if (self.agealter_doubleSpinBox.value() != 0):
            agealter = str(self.agealter_doubleSpinBox.value())
        else:
            agealter =agealter
        print(agealter)
        if (self.nationalter_textEdit.toPlainText() != ''):
            nationalter = self.nationalter_textEdit.toPlainText()
        else:
            nationalter =nationalter
        print(nationalter)
        if (self.positionalter_textEdit.toPlainText() != ''):
            positionalter = self.positionalter_textEdit.toPlainText()
        else:
            positionalter =positionalter
        print(positionalter)
        if (self.locationalter_textEdit.toPlainText() != ''):
            locationalter = self.locationalter_textEdit.toPlainText()
        else:
            locationalter =locationalter
        print(locationalter)
        if (self.kindalter_radioButton_1.isChecked() == True):
            kindalter = '口腔全景片'
        elif(self.kindalter_radioButton_2.isChecked() == True):
            kindalter = '头颅侧位片'
        elif(self.kindalter_radioButton_3.isChecked() == True):
            kindalter = 'CBCT'
        else:
            kindalter = kindalter
        print(genderalter)


        # SQL 更新语句
        sql = "UPDATE graphs SET name = '" + namealter \
              +"' , gender = '" + genderalter \
              +"' , age = "  + agealter\
              +" , nation = '" + nationalter \
              +"' , position = '" + positionalter \
              +"' , location = '" + locationalter \
              +"' , kind = '" + kindalter \
              +"' WHERE name = '" + self.namesearch_textEdit.toPlainText()\
              +"' OR id = " + self.IDsearch_textEdit.toPlainText() +""
        print(sql)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('数据更新成功！')
            self.result_textBrowser.setText('数据更新成功！')
        except:
            # 发生错误时回滚
            db.rollback()
            self.result_textBrowser.setText('数据更新失败！')

        # 关闭数据库连接
        db.close()

        '''
        连接成功！
        数据更新成功！
        '''

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle(_translate("main", "口腔头颈影像数据库管理窗口"))
        self.title.setText(_translate("Form", "修改影像资料"))
        self.namesearch_label.setText(_translate("Form", "姓名查询："))
        self.IDsearch_label.setText(_translate("Form", "ID查询："))
        self.namealter_label.setText(_translate("Form", "姓名修改："))
        self.genderalter_label.setText(_translate("Form", "性别修改："))
        self.manalter_radioButton.setText(_translate("Form", "男"))
        self.womanalter_radioButton.setText(_translate("Form", "女"))
        self.agealter_label.setText(_translate("Form", "年龄修改："))
        self.nationalter_label.setText(_translate("Form", "民族修改："))
        self.locationalter_label.setText(_translate("Form", "图片地址修改："))
        self.locationalter_pushButton.setText(_translate("Form", "选择"))
        self.alter_pushButton.setText(_translate("Form", "修改"))
        self.return_pushButton.setText(_translate("Form", "返回上一页"))
        self.IDsearch_textEdit.setText(_translate("Form", "0"))
        self.positionnalter_label.setText(_translate("Form", "地区修改："))
        self.kindalter_label.setText(_translate("Form", "影像资料类型修改："))
        self.kindalter_radioButton_1.setText(_translate("Form", "口腔全景片"))
        self.kindalter_radioButton_2.setText(_translate("Form", "头颅侧位片"))
        self.kindalter_radioButton_3.setText(_translate("Form", "CBCT"))
