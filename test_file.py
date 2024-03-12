import sqlite3
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QMessageBox, QLineEdit, \
    QSpinBox



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QTableWidget(self.centralwidget)
        self.tableView.setGeometry(30, 110, 739, 431)

        self.comboBox_warehouses = QComboBox(self.centralwidget)
        self.comboBox_warehouses.setGeometry(QtCore.QRect(420, 40, 221, 62))
        self.comboBox_warehouses.setObjectName("comboBox_warehouses")

        self.filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_button.setGeometry(QtCore.QRect(30, 15, 151, 32))
        self.filter_button.setObjectName("filter_button")
        self.filter_button.setText("Применить фильтр")


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

        self.filter_line_edit = QLineEdit(self.centralwidget)
        self.filter_line_edit.setGeometry(QtCore.QRect(30, 50, 321, 42))
        self.filter_line_edit.setPlaceholderText("Фильтр поиска")






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())