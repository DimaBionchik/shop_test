
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


from dialog import Ui_Dialogg
from operation import Ui_Operation
from main import Ui_MainWindows
from sclad import Ui_Dialoggg
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(190, 20, 441, 521))
        self.tableView.setObjectName("tableView")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 20, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(643, 48, 151, 101))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(649, 169, 141, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 139, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 300, 151, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 330, 151, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 500, 151, 32))
        self.pushButton_9.setObjectName("pushButton_10")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 500, 151, 32))
        self.pushButton_10.setObjectName("pushButton_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 290, 151, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 151, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_dialog)
        self.pushButton_3.clicked.connect(self.open_operation_dialog)
        self.pushButton_11.clicked.connect(self.open_main_win)
        self.pushButton_4.clicked.connect(self.open_main_win)



    def open_main_win(self):
        dialog = QtWidgets.QDialog()
        main_win = Ui_Dialoggg()
        main_win.setupUi(dialog)
        result = dialog.exec_()


    def open_operation_dialog(self):
        dialog = QtWidgets.QDialog()
        ui_operation = Ui_Operation()
        ui_operation.setupUi(dialog)
        result = dialog.exec_()
    def open_dialog(self):
        dialog = QtWidgets.QDialog()
        ui_dialog = Ui_Dialogg()
        ui_dialog.setupUi(dialog)
        result = dialog.exec_()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "Склад"))
        self.pushButton_7.setText(_translate("MainWindow", "Добавить в корзину"))
        self.pushButton_8.setText(_translate("MainWindow", "Кол-во товара"))
        self.pushButton_9.setText(_translate("MainWindow", "Поиск"))
        self.pushButton.setText(_translate("MainWindow", "Клиенты"))
        self.pushButton_2.setText(_translate("MainWindow", "Продукты "))
        self.pushButton_3.setText(_translate("MainWindow", "Операции"))
        self.pushButton_4.setText(_translate("MainWindow", "Склады"))
        self.pushButton_5.setText(_translate("MainWindow", "Корзина"))
        self.pushButton_10.setText(_translate("MainWindow","В меню"))
        self.pushButton_11.setText(_translate("MainWindow","Таблицы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

