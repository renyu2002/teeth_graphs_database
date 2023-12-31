# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget


class Ui_Main(QWidget):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1172, 1042)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 430, 1151, 581))
        self.widget.setObjectName("widget")
        self.insert_pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.insert_pushButton_1.setEnabled(True)
        self.insert_pushButton_1.setGeometry(QtCore.QRect(0, 40, 551, 71))
        self.insert_pushButton_1.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.insert_pushButton_1.setObjectName("insert_pushButton_1")
        self.delete_pushButton = QtWidgets.QPushButton(self.widget)
        self.delete_pushButton.setEnabled(True)
        self.delete_pushButton.setGeometry(QtCore.QRect(310, 190, 551, 71))
        self.delete_pushButton.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.alter_pushButton = QtWidgets.QPushButton(self.widget)
        self.alter_pushButton.setEnabled(True)
        self.alter_pushButton.setGeometry(QtCore.QRect(310, 340, 551, 71))
        self.alter_pushButton.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.alter_pushButton.setObjectName("alter_pushButton")
        self.search_pushButton = QtWidgets.QPushButton(self.widget)
        self.search_pushButton.setEnabled(True)
        self.search_pushButton.setGeometry(QtCore.QRect(310, 490, 551, 71))
        self.search_pushButton.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.search_pushButton.setObjectName("search_pushButton")
        self.insert_pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.insert_pushButton_2.setEnabled(True)
        self.insert_pushButton_2.setGeometry(QtCore.QRect(600, 40, 551, 71))
        self.insert_pushButton_2.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.insert_pushButton_2.setObjectName("insert_pushButton_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(11, 11, 22, 22))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 1121, 81))
        self.label.setStyleSheet("font: 48pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 170, 1141, 231))
        self.widget_3.setObjectName("widget_3")
        self.host_label = QtWidgets.QLabel(self.widget_3)
        self.host_label.setGeometry(QtCore.QRect(30, 10, 51, 51))
        self.host_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.host_label.setObjectName("host_label")
        self.host_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.host_textEdit.setGeometry(QtCore.QRect(100, 10, 251, 51))
        self.host_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.host_textEdit.setObjectName("host_textEdit")
        self.port_label = QtWidgets.QLabel(self.widget_3)
        self.port_label.setGeometry(QtCore.QRect(380, 10, 101, 51))
        self.port_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.port_label.setObjectName("port_label")
        self.user_label = QtWidgets.QLabel(self.widget_3)
        self.user_label.setGeometry(QtCore.QRect(750, 10, 141, 51))
        self.user_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.user_label.setObjectName("user_label")
        self.pswd_label = QtWidgets.QLabel(self.widget_3)
        self.pswd_label.setGeometry(QtCore.QRect(0, 90, 91, 51))
        self.pswd_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.pswd_label.setObjectName("pswd_label")
        self.database_label = QtWidgets.QLabel(self.widget_3)
        self.database_label.setGeometry(QtCore.QRect(360, 90, 171, 51))
        self.database_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.database_label.setObjectName("database_label")
        self.table_label = QtWidgets.QLabel(self.widget_3)
        self.table_label.setGeometry(QtCore.QRect(780, 90, 111, 51))
        self.table_label.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.table_label.setObjectName("table_label")
        self.port_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.port_textEdit.setGeometry(QtCore.QRect(480, 10, 251, 51))
        self.port_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.port_textEdit.setObjectName("port_textEdit")
        self.user_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.user_textEdit.setGeometry(QtCore.QRect(890, 10, 251, 51))
        self.user_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.user_textEdit.setObjectName("user_textEdit")
        self.pswd_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.pswd_textEdit.setGeometry(QtCore.QRect(90, 90, 251, 51))
        self.pswd_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.pswd_textEdit.setObjectName("pswd_textEdit")
        self.database_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.database_textEdit.setGeometry(QtCore.QRect(540, 90, 221, 51))
        self.database_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.database_textEdit.setObjectName("database_textEdit")
        self.table_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.table_textEdit.setGeometry(QtCore.QRect(890, 90, 251, 51))
        self.table_textEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.table_textEdit.setObjectName("table_textEdit")
        self.settings_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.settings_pushButton.setGeometry(QtCore.QRect(380, 160, 371, 61))
        self.settings_pushButton.setStyleSheet("font: 24pt \"微软雅黑\";")
        self.settings_pushButton.setObjectName("settings_pushButton")
        self.settings_pushButton.clicked.connect(self.settings)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def settings(self):
        host = self.host_textEdit.toPlainText()
        port = self.port_textEdit.toPlainText()
        name = self.user_textEdit.toPlainText()
        pswd = self.pswd_textEdit.toPlainText()
        db = self.database_textEdit.toPlainText()
        table = self.table_textEdit.toPlainText()

        if((host != '') & (port != '') & (name != '') & (pswd != '') & (db !='') & (table != '')):
            f = open('../bin/settings.txt', 'w')
            f.write(host + '\n')
            f.write(port + '\n')
            f.write(name + '\n')
            f.write(pswd + '\n')
            f.write(db + '\n')
            f.write(table + '\n')
            f.close()


    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        main.setWindowTitle(_translate("Form", "口腔头颈影像数据库管理窗口"))
        self.insert_pushButton_1.setText(_translate("main", "增加数据"))
        self.delete_pushButton.setText(_translate("main", "删除数据"))
        self.alter_pushButton.setText(_translate("main", "修改数据"))
        self.search_pushButton.setText(_translate("main", "查询数据"))
        self.insert_pushButton_2.setText(_translate("main", "批量增加数据"))
        self.label.setText(_translate("main", "欢迎使用口腔头颈影像管理系统"))
        self.host_label.setText(_translate("main", "IP:"))
        self.port_label.setText(_translate("main", "端口:"))
        self.user_label.setText(_translate("main", "用户名:"))
        self.pswd_label.setText(_translate("main", "密码:"))
        self.database_label.setText(_translate("main", "数据库名:"))
        self.table_label.setText(_translate("main", "表名:"))
        self.settings_pushButton.setText(_translate("main", "确定"))
