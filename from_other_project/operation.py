import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from scroll import Scroll
from scroll_delete import Scroll_delete
from scroll_move import Scroll_move
from get_items_dialog import Scroll_get
from new_design1 import Get_prod
from sell_new_window import Sell_prod

class Ui_Operation(object):
    def __init__(self):
        self.loadFieldNamesAndTypes()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 599)
        self.scroll_delete = Scroll_delete()
        self.scroll = Sell_prod()
        self.scroll_move = Scroll_move()
        self.scroll_get = Get_prod()
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 251))
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
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 490, 151, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 125, 16))
        self.label.setObjectName("label")

        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(210, 40, 91, 251))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 40, 311, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(215, 21, 421, 501))
        self.tableView.setObjectName("tableView")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 20, 141, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton.clicked.connect(self.show_inner_dialog)
        self.pushButton_4.clicked.connect(self.delete_dialog)
        self.pushButton_3.clicked.connect(self.move_dialog)
        self.pushButton_2.clicked.connect(self.get_dialog)
        self.pushButton_10.clicked.connect(Dialog.reject)
        self.pushButton_11.clicked.connect(self.load)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def get_dialog(self):
        self.scroll_get.exec_()
    def move_dialog(self):
        self.scroll_move.exec_()

    def delete_dialog(self):
        self.scroll_delete.exec_()

    def show_inner_dialog(self):
        self.scroll.exec_()

    def loadFieldNamesAndTypes(self):
        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Операции"
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
        table_name = "Операции"
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


    def load(self):
         self.loadFieldNamesAndTypes()
         self.create_table_columns()
         self.load_data_from_db()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Продажа"))
        self.pushButton_2.setText(_translate("Dialog", "Приемка товара"))
        self.pushButton_3.setText(_translate("Dialog", "Перемещение"))
        self.pushButton_4.setText(_translate("Dialog", "Списание товара"))
        self.pushButton_10.setText(_translate("Dialog", "Главное меню"))
        self.pushButton_11.setText(_translate("Dialog", "Обновить"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Operation()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




