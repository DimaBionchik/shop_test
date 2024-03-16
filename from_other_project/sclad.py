
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtGui, QtCore

from create_data_base import Data_base_meth
from record_dialog import AddRecordDialog
from delete_window import ConfirmationDialog
from edit_record import EditRecordDialog




class Ui_Dialoggg(object):
    def __init__(self):
        self.field_names = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 599)
        self.my_db  =Data_base_meth()
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 151, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(620, 10, 169, 291))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(180, 10, 441, 521))
        self.tableView.setObjectName("tableView")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 490, 151, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 490, 169, 32))
        self.pushButton_11.setObjectName("pushButton_11")

        self.search_line_edit = QtWidgets.QLineEdit(Dialog)
        self.search_line_edit.setObjectName("search_line_edit")
        self.verticalLayout.addWidget(self.search_line_edit)



        self.pushButton_11.clicked.connect(self.search_data)

        self.pushButton_6.clicked.connect(self.update_data_base)
        self.pushButton_10.clicked.connect(Dialog.reject)
        self.pushButton_7.clicked.connect(self.show_add_record_dialog)
        self.pushButton_8.clicked.connect(self.show_confirmation_dialog)
        self.pushButton_9.clicked.connect(self.show_edit_dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def update_search_results(self, results):
        model = self.tableView.model()
        model.setRowCount(0)

        for row_index, row_data in enumerate(results):
            model.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QtGui.QStandardItem(str(col_data))
                model.setItem(row_index, col_index, item)
    def search_data(self):
        keyword = self.search_line_edit.text()
        if keyword:
            result = self.my_db.search_in_db(keyword)
            self.update_search_results(result)
    def show_add_record_dialog(self):
        self.loadFieldNamesAndTypes()

        dialog = AddRecordDialog(self.field_names)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            data = dialog.get_data()
            print(data)
            self.my_db.insert_sklad_data(data[0],data[1],data[2])

            print(data)
    def update_data_base(self):
        self.loadFieldNamesAndTypes()
        self.create_table_columns()
        self.load_data_from_db()

    def loadFieldNamesAndTypes(self):
        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Склады"
        sqlc = f"PRAGMA table_info({table_name})"
        field_info = list(cur.execute(sqlc))
        self.field_names = [info[1] for info in field_info]
        conne.close()
    def create_table_columns(self):
        model = QtGui.QStandardItemModel()
        self.tableView.setModel(model)

        for field_name in self.field_names:
            header_item = QtGui.QStandardItem(field_name)
            model.setHorizontalHeaderItem(model.columnCount(), header_item)

    def load_data_from_db(self):
        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Склады"
        sql_query = f"SELECT * FROM {table_name}"
        data = cur.execute(sql_query).fetchall()

        model = self.tableView.model()
        model.setRowCount(0)

        for row_index, row_data in enumerate(data):
            model.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QtGui.QStandardItem(str(col_data))
                model.setItem(row_index, col_index, item)
        conne.close()

    def show_confirmation_dialog(self):
        confirmation_dialog = ConfirmationDialog()
        result = confirmation_dialog.exec_()
        if result == QDialog.Accepted:
            selected_index = self.tableView.currentIndex()
            if selected_index.isValid():
                selected_id = self.tableView.model().index(selected_index.row(), 0).data()
                self.delete_record(selected_id)

    def delete_record(self, record_id):
        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Склады"
        sql_query = f"DELETE FROM {table_name} WHERE id = ?"
        cur.execute(sql_query, (record_id,))

        conne.commit()
        conne.close()


        self.update_data_base()

    def show_edit_dialog(self):

        selected_index = self.tableView.currentIndex()

        if selected_index.isValid():

            selected_data = [self.tableView.model().index(selected_index.row(), col).data()
                             for col in range(self.tableView.model().columnCount())]


            edit_dialog = EditRecordDialog(self.field_names, selected_data)
            result = edit_dialog.exec_()

            if result == QDialog.Accepted:
                new_data = edit_dialog.get_new_data()


                self.update_record(selected_data[0], new_data)

    def update_record(self, record_id, new_data):
        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Склады"


        set_params = ', '.join([f"{field} = ?" for field in self.field_names[1:]])


        sql_query = f"UPDATE {table_name} SET {set_params} WHERE id = ?"


        cur.execute(sql_query, new_data + [record_id])

        conne.commit()
        conne.close()


        self.update_data_base()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Клиенты"))
        self.pushButton_2.setText(_translate("Dialog", "Продукты "))
        self.pushButton_3.setText(_translate("Dialog", "Операции"))
        self.pushButton_4.setText(_translate("Dialog", "Склады"))
        self.pushButton_5.setText(_translate("Dialog", "Корзина"))
        self.pushButton_6.setText(_translate("Dialog", "Обновить "))
        self.pushButton_7.setText(_translate("Dialog", "Добавить"))
        self.pushButton_8.setText(_translate("Dialog", "Удалить"))
        self.pushButton_9.setText(_translate("Dialog", "Изменить "))
        self.pushButton_10.setText(_translate("Dialog", "Главное меню"))
        self.pushButton_11.setText(_translate("Dialog", "Поиск"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialoggg()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
