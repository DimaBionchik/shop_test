import sqlite3
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QMessageBox, QLineEdit, \
    QSpinBox



class Ui_MainWindows(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 599)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 151, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.sort_order = Qt.AscendingOrder

        self.tableView = QTableWidget(self.layoutWidget)
        self.tableView.setGeometry(30, 110, 739, 431)

        self.comboBox_warehouses = QComboBox(self.layoutWidget)
        self.comboBox_warehouses.setGeometry(QtCore.QRect(420, 40, 221, 62))
        self.comboBox_warehouses.setObjectName("comboBox_warehouses")

        self.filter_button = QtWidgets.QPushButton(self.layoutWidget)
        self.filter_button.setGeometry(QtCore.QRect(30, 15, 151, 32))
        self.filter_button.setObjectName("filter_button")
        self.filter_button.setText("Применить фильтр")


        # Dialog.setCentralWidget(self.layoutWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.filter_line_edit = QLineEdit(self.layoutWidget)
        self.filter_line_edit.setGeometry(QtCore.QRect(30, 50, 321, 42))
        self.filter_line_edit.setPlaceholderText("Фильтр поиска")
        self.get_table_names()
        self.comboBox_warehouses.currentIndexChanged.connect(self.load_table)
        self.filter_button.clicked.connect(self.search_data)
        self.tableView.horizontalHeader().sectionClicked.connect(self.sort_column)

    def load_table(self):
        selected_table = self.comboBox_warehouses.currentText()

        if selected_table == "Выбери таблицу":
            return

        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()

        # Получаем информацию о структуре таблицы, включая вычисляемые столбцы
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{selected_table}'")
        table_info = cursor.fetchone()
        if table_info:
            table_definition = table_info[0]
            generated_columns = [line.split('GENERATED ALWAYS AS')[0].strip() for line in table_definition.split('\n')
                                 if 'GENERATED ALWAYS AS' in line]
        else:
            generated_columns = []

        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        self.tableView.setColumnCount(len(column_names))
        self.tableView.setHorizontalHeaderLabels(column_names)

        self.tableView.clearContents()
        self.tableView.setRowCount(0)

        self.tableView.setRowCount(len(data))
        self.tableView.setColumnCount(len(column_names))

        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                # Если столбец - info_prod, то используем его значение
                if column_names[col] in generated_columns:
                    item = QTableWidgetItem(str(col_data))
                else:
                    item = QTableWidgetItem(str(col_data))
                self.tableView.setItem(row, col, item)

        con.close()

    def search_data(self):
        selected_table = self.comboBox_warehouses.currentText()
        search_text = self.filter_line_edit.text()

        if selected_table == "Выбери таблицу":
            return
        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()

        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{selected_table}'")
        table_info = cursor.fetchone()
        if table_info:
            table_definition = table_info[0]
            generated_columns = [line.split('GENERATED ALWAYS AS')[0].strip() for line in table_definition.split('\n')
                                 if 'GENERATED ALWAYS AS' in line]
        else:
            generated_columns = []

        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        # Фильтрация данных по поисковому запросу
        if search_text:
            filtered_data = [row for row in data if any(str(search_text) in str(cell) for cell in row)]
        else:
            filtered_data = data

        self.tableView.clearContents()
        self.tableView.setRowCount(0)

        self.tableView.setRowCount(len(filtered_data))
        self.tableView.setColumnCount(len(column_names))

        self.tableView.setHorizontalHeaderLabels(column_names)

        for row, row_data in enumerate(filtered_data):
            for col, col_data in enumerate(row_data):
                if column_names[col] in generated_columns:
                    item = QTableWidgetItem(str(col_data))
                else:
                    item = QTableWidgetItem(str(col_data))
                self.tableView.setItem(row, col, item)

        con.close()

    def sort_column(self, logical_index):
        selected_table = self.comboBox_warehouses.currentText()
        if selected_table == "Выбери таблицу":
            return

        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()

        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        sorted_data = sorted(data, key=lambda x: x[logical_index])

        if self.sort_order == Qt.AscendingOrder:
            self.sort_order = Qt.DescendingOrder
            sorted_data.reverse()
        else:
            self.sort_order = Qt.AscendingOrder

        self.tableView.clearContents()
        self.tableView.setRowCount(0)

        self.tableView.setRowCount(len(sorted_data))
        self.tableView.setColumnCount(len(column_names))

        self.tableView.setHorizontalHeaderLabels(column_names)

        for row, row_data in enumerate(sorted_data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableView.setItem(row, col, item)

        con.close()

    def get_table_names(self):
        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        names = [table[0] for table in tables if table[0].istitle()]

        self.comboBox_warehouses.clear()
        self.comboBox_warehouses.addItem("Выбери таблицу")
        self.comboBox_warehouses.addItems(names)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("MainWindow", "Главное меню"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())