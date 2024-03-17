import ast
import json
import sqlite3
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QMessageBox, QLineEdit, \
    QSpinBox
from finalll import Ui_MainWindows as MainUi


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort_order = Qt.AscendingOrder
        # self.child_main_window = QtWidgets.QMainWindow()
        # self.child_ui = MainUi()
        # self.child_ui.setupUi(self.child_main_window)
        self.tableView = QTableWidget(self.centralwidget)
        self.tableView.setGeometry(30, 110, 739, 431)

        self.comboBox_warehouses = QComboBox(self.centralwidget)
        self.comboBox_warehouses.setGeometry(QtCore.QRect(420, 40, 221, 62))
        self.comboBox_warehouses.setObjectName("comboBox_warehouses")

        self.filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_button.setGeometry(QtCore.QRect(30, 15, 151, 32))
        self.filter_button.setObjectName("filter_button")
        self.filter_button.setText("Применить фильтр")
        self.filter_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.filter_button1.setGeometry(QtCore.QRect(200, 15, 151, 32))
        self.filter_button1.setObjectName("some_button")
        self.filter_button1.setText("some button")

        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(420, 15, 151, 32))
        self.main_button.setObjectName("filter_button")
        self.main_button.setText("Главное меню")
        self.main_button.setVisible(False)


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
        self.get_table_names()
        self.comboBox_warehouses.currentIndexChanged.connect(self.load_table)
        self.filter_button.clicked.connect(self.search_data)
        self.tableView.horizontalHeader().sectionClicked.connect(self.sort_column)
        self.tableView.clicked.connect(self.show_warning)
        self.main_button.clicked.connect(self.load_table)
        self.filter_button1.clicked.connect(self.open_dealog_window)




    def open_dealog_window(self):
        self.child_main_window = QtWidgets.QMainWindow()
        self.child_ui = MainUi()
        self.child_ui.setupUi(self.child_main_window)
        self.child_main_window.show()

    def load_table(self):
        selected_table = self.comboBox_warehouses.currentText()

        if selected_table == "Выбери таблицу":
            return

        self.main_button.setVisible(False)

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

        cursor.execute(f"PRAGMA table_info({selected_table})")
        column_info = cursor.fetchall()
        column_names = [col[1] for col in column_info]

        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        if 'busket' in column_names:
            busket_index = column_names.index('busket')
            column_names.pop(busket_index)
            data_end = [tuple(item[:-1]) for item in data]
        else:
            data_end = data

        if selected_table == 'Покупка':
            self.replace_client_ids_with_names(data_end, column_names, cursor)

        if selected_table == 'Поставка':
            self.replace_warehouse_ids_with_names(data_end, column_names, cursor)

        self.tableView.setColumnCount(len(column_names))
        self.tableView.setHorizontalHeaderLabels(column_names)

        self.tableView.clearContents()
        self.tableView.setRowCount(0)

        self.tableView.setRowCount(len(data_end))
        self.tableView.setColumnCount(len(column_names))

        for row, row_data in enumerate(data_end):
            for col, col_data in enumerate(row_data):
                if column_names[col] in generated_columns:
                    item = QTableWidgetItem(str(col_data))
                else:
                    item = QTableWidgetItem(str(col_data))
                self.tableView.setItem(row, col, item)

        con.close()

    def replace_client_ids_with_names(self, data, column_names, cursor):
        client_name_dict = dict(cursor.execute("SELECT id, FIO FROM Клиенты").fetchall())
        for i, row in enumerate(data):
            client_id = row[column_names.index('client_id')]
            if client_id in client_name_dict:
                data[i] = list(row)
                data[i][column_names.index('client_id')] = client_name_dict[client_id]

    def replace_warehouse_ids_with_names(self, data, column_names, cursor):
        warehouse_name_dict = dict(cursor.execute("SELECT id, name FROM Склады").fetchall())
        for i, row in enumerate(data):
            warehouse_id = row[column_names.index('warehouse_id')]
            if warehouse_id in warehouse_name_dict:
                data[i] = list(row)
                data[i][column_names.index('warehouse_id')] = warehouse_name_dict[warehouse_id]

    def search_data(self):
        search_text = self.filter_line_edit.text().lower()

        row_count = self.tableView.rowCount()
        col_count = self.tableView.columnCount()

        for row in range(row_count):
            row_visible = False
            for col in range(col_count):
                item = self.tableView.item(row, col)
                if item is not None and search_text in item.text().lower():
                    row_visible = True
                    break
            self.tableView.setRowHidden(row, not row_visible)

    def sort_column(self, logical_index):
        selected_table = self.comboBox_warehouses.currentText()
        if selected_table == "Выбери таблицу":
            return

        visible_rows = [row for row in range(self.tableView.rowCount()) if not self.tableView.isRowHidden(row)]

        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()

        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        visible_columns = self.tableView.model().columnCount()

        sorted_data = []

        for row_index in visible_rows:
            row_data = [self.tableView.item(row_index, col_index).text() for col_index in range(visible_columns)]
            sorted_data.append(row_data)

        sorted_data.sort(key=lambda x: x[logical_index])

        if self.sort_order == Qt.AscendingOrder:
            self.sort_order = Qt.DescendingOrder
            sorted_data.reverse()
        else:
            self.sort_order = Qt.AscendingOrder

        self.tableView.clearContents()
        self.tableView.setRowCount(0)

        self.tableView.setRowCount(len(sorted_data))
        self.tableView.setColumnCount(visible_columns)

        column_names = [description[0] for description in cursor.description]
        self.tableView.setHorizontalHeaderLabels(column_names)

        for row, row_data in enumerate(sorted_data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableView.setItem(row, col, item)

        con.close()


    #
    # def show_warning(self, index):
    #     row = index.row()
    #     selected_table = self.comboBox_warehouses.currentText()
    #
    #     if selected_table not in ["Покупка", "Поставка", "Склады"]:
    #         return
    #     if selected_table == 'Склады':
    #         reply = QMessageBox.question(MainWindow, 'Просмотр склада',
    #                                      'Хотите ли вы посмотреть содержимое этого склада?',
    #                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     else:
    #         reply = QMessageBox.question(MainWindow, 'Просмотр содержимого',
    #                                      'Хотите ли вы посмотреть содержимое этой записи?',
    #                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         con = sqlite3.connect('new_bd.db')
    #         cursor = con.cursor()
    #
    #         id_value = self.tableView.item(row, 0).text()
    #         cursor.execute(f"SELECT busket FROM {selected_table} WHERE id=?", (id_value,))
    #         busket_info = cursor.fetchone()
    #
    #         con.close()
    #
    #         if busket_info:
    #             busket_content = busket_info[0]
    #
    #             # Проверяем, если словарь неправильного формата
    #             if not isinstance(busket_content, dict):
    #                 QMessageBox.warning(MainWindow, 'Ошибка', 'Формат корзины недействителен')
    #                 return
    #
    #             # Создаем заголовки таблицы
    #             self.tableView.setRowCount(len(busket_content))
    #             self.tableView.setColumnCount(2)
    #             self.tableView.setHorizontalHeaderLabels(["Название товара", "Количество"])
    #             self.main_button.setVisible(True)
    #
    #             # Заполняем таблицу данными из словаря
    #             for i, (product, quantity) in enumerate(busket_content.items()):
    #                 self.tableView.setItem(i, 0, QTableWidgetItem(product))
    #                 self.tableView.setItem(i, 1, QTableWidgetItem(str(quantity)))
    #
    #         else:
    #             QMessageBox.information(MainWindow, 'Содержимое корзины', f'Корзина для ID {id_value} пуста')

    def show_warning(self, index):
        row = index.row()
        selected_table = self.comboBox_warehouses.currentText()

        if selected_table not in ["Покупка", "Поставка", "Склады"]:
            return

        if selected_table == 'Склады':
            reply = QMessageBox.question(MainWindow, 'Просмотр склада',
                                         'Хотите ли вы посмотреть содержимое этого склада?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.question(MainWindow, 'Просмотр содержимого',
                                         'Хотите ли вы посмотреть содержимое этой записи?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            con = sqlite3.connect('new_bd.db')
            cursor = con.cursor()

            id_value = self.tableView.item(row, 0).text()
            cursor.execute(f"SELECT busket FROM {selected_table} WHERE id=?", (id_value,))
            busket_info = cursor.fetchone()

            con.close()

            if busket_info:
                try:
                    # Преобразуем строку в словарь с помощью ast.literal_eval()
                    busket_content = ast.literal_eval(busket_info[0])

                    # Устанавливаем количество строк в таблице
                    self.tableView.setRowCount(len(busket_content))

                    # Устанавливаем заголовки столбцов
                    self.tableView.setHorizontalHeaderLabels(["Название товара", "Код", "Количество"])

                    # Заполняем таблицу данными из словаря
                    row = 0
                    for product, parameters in busket_content.items():
                        for parameter, value in parameters.items():
                            self.tableView.setItem(row, 0, QTableWidgetItem(product))
                            self.tableView.setItem(row, 1, QTableWidgetItem(parameter))
                            self.tableView.setItem(row, 2, QTableWidgetItem(str(value)))
                            row += 1
                except (ValueError, SyntaxError) as e:
                    QMessageBox.warning(MainWindow, 'Ошибка', f'Неправильный формат данных для корзины: {e}')
            else:
                QMessageBox.warning(MainWindow, 'Ошибка', f'Содержимое корзины для ID {id_value} не найдено')
    def get_table_names(self):
        con = sqlite3.connect('new_bd.db')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        names = [table[0] for table in tables if table[0].istitle()]

        self.comboBox_warehouses.clear()
        self.comboBox_warehouses.addItem("Выбери таблицу")
        self.comboBox_warehouses.addItems(names)


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


