# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget
import pymysql
import os , shutil
import pandas as pd


class Ui_Search(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1252, 1015)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(390, 0, 481, 81))
        self.title.setStyleSheet("font: 48pt \"微软雅黑\";")
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 90, 511, 81))
        self.widget.setObjectName("widget")
        self.ID_label = QtWidgets.QLabel(self.widget)
        self.ID_label.setGeometry(QtCore.QRect(30, 20, 71, 51))
        self.ID_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.ID_label.setObjectName("ID_label")
        self.ID_textEdit = QtWidgets.QTextEdit(self.widget)
        self.ID_textEdit.setGeometry(QtCore.QRect(100, 20, 381, 51))
        self.ID_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.ID_textEdit.setObjectName("ID_textEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 80, 1241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 180, 511, 81))
        self.widget_2.setObjectName("widget_2")
        self.name_label = QtWidgets.QLabel(self.widget_2)
        self.name_label.setGeometry(QtCore.QRect(30, 20, 101, 51))
        self.name_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.name_label.setObjectName("name_label")
        self.name_textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.name_textEdit.setGeometry(QtCore.QRect(140, 20, 341, 51))
        self.name_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.name_textEdit.setObjectName("name_textEdit")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(30, 270, 511, 81))
        self.widget_3.setObjectName("widget_3")
        self.gender_label = QtWidgets.QLabel(self.widget_3)
        self.gender_label.setGeometry(QtCore.QRect(30, 10, 101, 51))
        self.gender_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.gender_label.setObjectName("gender_label")
        self.man_radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.man_radioButton.setGeometry(QtCore.QRect(160, 10, 115, 19))
        self.man_radioButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.man_radioButton.setObjectName("man_radioButton")
        self.woman_radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.woman_radioButton.setGeometry(QtCore.QRect(160, 50, 115, 19))
        self.woman_radioButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.woman_radioButton.setObjectName("woman_radioButton")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(30, 360, 511, 171))
        self.widget_4.setObjectName("widget_4")
        self.age_label = QtWidgets.QLabel(self.widget_4)
        self.age_label.setGeometry(QtCore.QRect(20, 60, 111, 51))
        self.age_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.age_label.setObjectName("age_label")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 72, 15))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.from_label = QtWidgets.QLabel(self.widget_4)
        self.from_label.setGeometry(QtCore.QRect(140, 20, 61, 51))
        self.from_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.from_label.setObjectName("from_label")
        self.to_label = QtWidgets.QLabel(self.widget_4)
        self.to_label.setGeometry(QtCore.QRect(140, 110, 61, 51))
        self.to_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.to_label.setObjectName("to_label")
        self.from_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.from_doubleSpinBox.setGeometry(QtCore.QRect(240, 20, 141, 51))
        self.from_doubleSpinBox.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.from_doubleSpinBox.setObjectName("from_doubleSpinBox")
        self.to_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.to_doubleSpinBox.setGeometry(QtCore.QRect(240, 110, 141, 51))
        self.to_doubleSpinBox.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.to_doubleSpinBox.setObjectName("to_doubleSpinBox")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(590, 90, 20, 851))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.result_textBrowser = QtWidgets.QTextBrowser(Form)
        self.result_textBrowser.setGeometry(QtCore.QRect(640, 110, 591, 811))
        self.result_textBrowser.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.result_textBrowser.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 940, 1251, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.search_pushButton = QtWidgets.QPushButton(Form)
        self.search_pushButton.setGeometry(QtCore.QRect(60, 960, 631, 41))
        self.search_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.search_pushButton.setObjectName("search_pushButton")
        self.search_pushButton.clicked.connect(self.search)
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(30, 850, 571, 81))
        self.widget_5.setObjectName("widget_5")
        self.save_label = QtWidgets.QLabel(self.widget_5)
        self.save_label.setGeometry(QtCore.QRect(10, 20, 131, 51))
        self.save_label.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.save_label.setObjectName("save_label")
        self.save_textEdit = QtWidgets.QTextEdit(self.widget_5)
        self.save_textEdit.setGeometry(QtCore.QRect(140, 20, 341, 51))
        self.save_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.save_textEdit.setObjectName("save_textEdit")
        self.save_pushButton = QtWidgets.QPushButton(self.widget_5)
        self.save_pushButton.setGeometry(QtCore.QRect(500, 20, 61, 51))
        self.save_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.save_pushButton.setObjectName("save_pushButton")
        self.save_pushButton.clicked.connect(self.locate)
        self.return_pushButton = QtWidgets.QPushButton(Form)
        self.return_pushButton.setGeometry(QtCore.QRect(740, 960, 441, 41))
        self.return_pushButton.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.return_pushButton.setObjectName("return_pushButton")
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(30, 630, 511, 81))
        self.widget_6.setObjectName("widget_6")
        self.position_label = QtWidgets.QLabel(self.widget_6)
        self.position_label.setGeometry(QtCore.QRect(30, 20, 101, 51))
        self.position_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.position_label.setObjectName("position_label")
        self.position_textEdit = QtWidgets.QTextEdit(self.widget_6)
        self.position_textEdit.setGeometry(QtCore.QRect(140, 20, 341, 51))
        self.position_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.position_textEdit.setObjectName("position_textEdit")
        self.widget_7 = QtWidgets.QWidget(Form)
        self.widget_7.setGeometry(QtCore.QRect(30, 540, 511, 81))
        self.widget_7.setObjectName("widget_7")
        self.nation_label = QtWidgets.QLabel(self.widget_7)
        self.nation_label.setGeometry(QtCore.QRect(30, 20, 101, 51))
        self.nation_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.nation_label.setObjectName("nation_label")
        self.nation_textEdit = QtWidgets.QTextEdit(self.widget_7)
        self.nation_textEdit.setGeometry(QtCore.QRect(140, 20, 341, 51))
        self.nation_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.nation_textEdit.setObjectName("nation_textEdit")
        self.widget_8 = QtWidgets.QWidget(Form)
        self.widget_8.setGeometry(QtCore.QRect(30, 720, 511, 121))
        self.widget_8.setObjectName("widget_8")
        self.kind_label = QtWidgets.QLabel(self.widget_8)
        self.kind_label.setGeometry(QtCore.QRect(10, 30, 271, 51))
        self.kind_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.kind_label.setObjectName("kind_label")
        self.kind_radioButton_1 = QtWidgets.QRadioButton(self.widget_8)
        self.kind_radioButton_1.setGeometry(QtCore.QRect(300, 10, 131, 21))
        self.kind_radioButton_1.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kind_radioButton_1.setObjectName("kind_radioButton_1")
        self.kind_radioButton_2 = QtWidgets.QRadioButton(self.widget_8)
        self.kind_radioButton_2.setGeometry(QtCore.QRect(300, 50, 131, 21))
        self.kind_radioButton_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kind_radioButton_2.setObjectName("kind_radioButton_2")
        self.kind_radioButton_3 = QtWidgets.QRadioButton(self.widget_8)
        self.kind_radioButton_3.setGeometry(QtCore.QRect(300, 90, 115, 19))
        self.kind_radioButton_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.kind_radioButton_3.setObjectName("kind_radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def locate(self):
        location = QtWidgets.QFileDialog.getExistingDirectory(None, "选取存储文件夹", "C:/")  # 起始路径
        location = str(location)
        location = location.replace('(','')
        location = location.replace(')','')
        location = location.replace(',','')
        location = location.replace("'",'')
        location = location.replace('All Files *','')
        location = location.strip()
        self.save_textEdit.setText(location)
    def pd_toExcel(self,data, fileName):  # pandas库储存数据到excel
        print("导入开始")
        ids = []
        names = []
        genders = []
        ages = []
        nations = []
        positions = []
        kinds = []
        for i in range(len(data)):
            ids.append(data[i]["id"])
            names.append(data[i]["name"])
            genders.append(data[i]["gender"])
            ages.append(data[i]["age"])
            nations.append(data[i]["nation"])
            positions.append(data[i]["position"])
            kinds.append(data[i]["kind"])

        dfData = {  # 用字典设置DataFrame所需数据
            '序号': ids,
            '姓名': names,
            '性别': genders,
            '年龄': ages,
            '民族': nations,
            '地区': positions,
            '影像资料类型': kinds
        }
        df = pd.DataFrame(dfData)  # 创建DataFrame
        df.to_excel(fileName)  # 存表，去除原始索引列（0,1,2...）
        print("导入成功")

    def search(self):

        ID = self.ID_textEdit.toPlainText()
        name = self.name_textEdit.toPlainText()
        gender = ''
        if (self.man_radioButton.isChecked() == True):
            gender = '男'
        elif (self.woman_radioButton.isChecked() == True):
            gender = '女'
        age = ''
        From = ''
        To = ''
        if (self.from_doubleSpinBox.value() == float(0) and self.to_doubleSpinBox.value() == float(0)):
            age = '0'
        else:
            age = ''
            From = str(self.from_doubleSpinBox.value())
            To =str( self.to_doubleSpinBox.value())
        nation = self.nation_textEdit.toPlainText()
        position = self.position_textEdit.toPlainText()
        kind = ''
        if (self.kind_radioButton_1.isChecked() == True):
            kind = '口腔全景片'
        elif (self.kind_radioButton_2.isChecked() == True):
            kind = '头颅侧位片'
        elif (self.kind_radioButton_3.isChecked() == True):
            kind = 'CBCT'
        distance = self.save_textEdit.toPlainText()

        # 打开数据库连接
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

        # SQL 查询语句
        sql = "SELECT * FROM "+table+" WHERE "
        if (ID != '0'):
            sql = sql + "id = " + ID + " AND "
        else:
            sql = sql + "id !=" + ID + " AND "
        if (name != ''):
            sql = sql + "name = '" + name + "' AND "
        else:
            sql = sql + "name != '" + name + "' AND "
        if (gender != ''):
            sql = sql + "gender = '" + gender + "' AND "
        else:
            sql = sql + "gender != '" + gender + "' AND "
        if (age != '0'):
            sql = sql + "age >= " + From + " AND age <= " + To +" AND "
        else:
            sql = sql + "age != " + age + " AND "
        if (nation != ''):
            sql = sql + "nation = '" + nation + "' AND "
        else:
            sql = sql + "nation != '" + nation + "' AND "
        if (position != ''):
            sql = sql + "position = '" + position + "' AND "
        else:
            sql = sql + "position != '" + position + "' AND "
        if (kind != ''):
            sql = sql + "kind = '" + kind + "'"
        else:
            sql = sql + "kind != '" + kind + "'"
        print(sql)

        data = []
        excel = distance + "/"+"口腔头颈影像"+"/"+ "影像数据.xlsx"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = '查询结果为:\n'
            results = cursor.fetchall()
            for row in results:
                ID = row[1]
                name = row[2]
                gender = row[3]
                age = str(row[4])
                nation = row[5]
                position = row[6]
                location = row[7]
                kind = row[8]
                # 打印结果
                result = result +"ID:%s,姓名:%s,性别:%s,年龄:%s,民族:%s,地区:%s，影像资料类型:%s\n" % (ID, name, gender, age,nation,position,kind)
                print(result)
                if not os.path.isfile(location):
                    print("%s not exist!" % (location))
                else:
                    distance = distance + "/"+"口腔头颈影像"+"/"+name+"_"+gender+"_"+age+"_"+nation+"_"+position+"_"+kind+location[-4:]
                    fpath, fname = os.path.split(distance)
                    if not os.path.exists(fpath):
                        os.makedirs(fpath)  # 创建路径
                    shutil.copy(location, distance)  # 复制文件
                    print ("copy %s -> %s" % (location, distance))
                    data.append({"id": ID,"name": name,"gender": gender,"age": age,"nation": nation,"position": position,"kind": kind})
                    print(data)
                    distance = self.save_textEdit.toPlainText()
        except:
            result = '查询失败'
        self.pd_toExcel(data, excel)
        self.result_textBrowser.setText(result)

        # 关闭数据库连接
        db.close()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle(_translate("Form", "口腔头颈影像数据库管理窗口"))
        self.title.setText(_translate("Form", "查询影像资料"))
        self.ID_label.setText(_translate("Form", "ID："))
        self.ID_textEdit.setText(_translate("Form", "0"))
        self.name_label.setText(_translate("Form", "姓名："))
        self.gender_label.setText(_translate("Form", "性别："))
        self.man_radioButton.setText(_translate("Form", "男"))
        self.woman_radioButton.setText(_translate("Form", "女"))
        self.age_label.setText(_translate("Form", "年龄："))
        self.from_label.setText(_translate("Form", "从："))
        self.to_label.setText(_translate("Form", "至："))
        self.search_pushButton.setText(_translate("Form", "查询"))
        self.save_label.setText(_translate("Form", "存放文件夹："))
        self.save_pushButton.setText(_translate("Form", "选择"))
        self.return_pushButton.setText(_translate("Form", "返回上一页"))
        self.position_label.setText(_translate("Form", "地区："))
        self.nation_label.setText(_translate("Form", "民族："))
        self.kind_label.setText(_translate("Form", "影像资料类型："))
        self.kind_radioButton_1.setText(_translate("Form", "口腔全景片"))
        self.kind_radioButton_2.setText(_translate("Form", "头颅侧位片"))
        self.kind_radioButton_3.setText(_translate("Form", "CBCT"))
