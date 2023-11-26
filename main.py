
from PyQt5 import QtWidgets
import sys
from UI.mainwindow import Ui_Main
from UI.insertwindow_1 import Ui_Insert_1
from UI.deletewindow import Ui_Delete
from UI.alterwindow import Ui_Alter
from UI.searchwindow import Ui_Search
from UI.insertwindow_2 import Ui_Insert_2


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_Main()
    ui_main.setupUi(mainWindow)

    insertWindow_1 = QtWidgets.QMainWindow()
    ui_insert_1 = Ui_Insert_1()
    ui_insert_1.setupUi(insertWindow_1)

    insertWindow_2 = QtWidgets.QMainWindow()
    ui_insert_2 = Ui_Insert_2()
    ui_insert_2.setupUi(insertWindow_2)

    deleteWindow = QtWidgets.QMainWindow()
    ui_delete = Ui_Delete()
    ui_delete.setupUi(deleteWindow)

    alterWindow = QtWidgets.QMainWindow()
    ui_alter = Ui_Alter()
    ui_alter.setupUi(alterWindow)

    searchWindow = QtWidgets.QMainWindow()
    ui_search = Ui_Search()
    ui_search.setupUi(searchWindow)


    ui_main.insert_pushButton_1.clicked.connect(insertWindow_1.show)
    ui_main.insert_pushButton_1.clicked.connect(mainWindow.close)

    ui_main.insert_pushButton_2.clicked.connect(insertWindow_2.show)
    ui_main.insert_pushButton_2.clicked.connect(mainWindow.close)

    ui_main.delete_pushButton.clicked.connect(deleteWindow.show)
    ui_main.delete_pushButton.clicked.connect(mainWindow.close)

    ui_main.alter_pushButton.clicked.connect(alterWindow.show)
    ui_main.alter_pushButton.clicked.connect(mainWindow.close)

    ui_main.search_pushButton.clicked.connect(searchWindow.show)
    ui_main.search_pushButton.clicked.connect(mainWindow.close)

    ui_insert_1.return_pushButton.clicked.connect(insertWindow_1.close)
    ui_insert_1.return_pushButton.clicked.connect(mainWindow.show)

    ui_insert_2.return_pushButton.clicked.connect(insertWindow_2.close)
    ui_insert_2.return_pushButton.clicked.connect(mainWindow.show)

    ui_delete.return_pushButton.clicked.connect(deleteWindow.close)
    ui_delete.return_pushButton.clicked.connect(mainWindow.show)

    ui_alter.return_pushButton.clicked.connect(alterWindow.close)
    ui_alter.return_pushButton.clicked.connect(mainWindow.show)

    ui_search.return_pushButton.clicked.connect(searchWindow.close)
    ui_search.return_pushButton.clicked.connect(mainWindow.show)


    mainWindow.show()

    sys.exit(app.exec_())
