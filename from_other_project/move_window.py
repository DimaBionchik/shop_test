import sqlite3
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QTextEdit, QScrollArea, QVBoxLayout, QPushButton, QLabel, QApplication, QLineEdit, \
    QMessageBox
from create_data_base import Data_base_meth
import os
from record_dialog import AddRecordDialog
from openpyxl import Workbook
from docx import Document
from datetime import date

class InputDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" количество товара")
        self.layout = QVBoxLayout()
        self.amount_label = QLabel("Количество:")
        self.amount_edit = QLineEdit()
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_edit)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

    def get_data(self):
        amount = self.amount_edit.text()
        return amount

class Move_product(QDialog):
    def __init__(self):
        super().__init__()
        self.my_db = Data_base_meth(database_name="new_bd.db")
        self.setupUi(self)
        self.name_text = ''
        self.name_text2 = ""
        self.name_text3 = ''
        self.sclad = ''
        self.basket ={}
        self.date_delivery =''
        self.final_price = 0
        self.personal =''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 405)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 125, 16))
        self.label.setObjectName("label")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 91, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(110, 30, 301, 31))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 29))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(110, 30, 299, 29))
        self.listWidget.setObjectName("listWidget")
        data = self.my_db.select_all_from_sclad()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(list_item)
        self.listWidget.itemClicked.connect(self.save_data_for_storage)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(110, 70, 301, 31))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 299, 29))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.listWidget2 = QtWidgets.QListWidget(Dialog)
        self.listWidget2.setGeometry(QtCore.QRect(110, 70, 301, 31))
        self.listWidget2.setObjectName("listWidget")
        data = self.my_db.select_all_from_db()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget2.addItem(list_item)
        self.listWidget2.itemClicked.connect(self.save_data_for_products)
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_3.setGeometry(QtCore.QRect(110, 120, 301, 31))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 299, 29))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.listWidget3 = QtWidgets.QListWidget(Dialog)
        self.listWidget3.setGeometry(QtCore.QRect(110, 120, 301, 31))
        self.listWidget3.setObjectName("listWidget")
        data = self.my_db.select_all_from_sclad()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget3.addItem(list_item)
        self.listWidget3.itemClicked.connect(self.save_data_for_storage2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 240, 401, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 60, 191, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(420, 20, 191, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.scrollArea_4 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_4.setGeometry(QtCore.QRect(110, 160, 301, 31))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 299, 29))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.listWidget4 = QtWidgets.QListWidget(Dialog)
        self.listWidget4.setGeometry(QtCore.QRect(110, 160, 301, 31))
        self.listWidget4.setObjectName("listWidget")
        data = self.my_db.select_all_from_client()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget4.addItem(list_item)
        self.listWidget4.itemClicked.connect(self.save_data_for_personal)
        self.textEdit_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.scrollArea_5 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_5.setGeometry(QtCore.QRect(110, 200, 301, 31))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 299, 29))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_5)
        self.textEdit_5.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        today = date.today()
        self.textEdit_5.setPlainText(str(today))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def delete_bag(self):
        self.plainTextEdit.setPlainText("")
        self.basket.clear()
        self.final_price =0
    def show_notification(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Уведомление")
        msg_box.setText(message)
        msg_box.exec_()
    def loadFieldNamesAndTypes(self,table_names):

        conne = sqlite3.connect("new_bd.db")
        cur = conne.cursor()
        table_name = table_names
        sqlc = f"PRAGMA table_info({table_name})"
        field_info = list(cur.execute(sqlc))
        self.field_names = [info[1] for info in field_info]
        conne.close()

    def show_input_data_dialog(self, name_text):
        input_dialog = InputDataDialog()

        if input_dialog.exec_() == QDialog.Accepted:
            amount = input_dialog.get_data()
            current_text = self.plainTextEdit.toPlainText()
            price = self.my_db.select_price(name_text)
            product_price = (int(price) * int(amount))
            self.final_price += product_price

            new_text = current_text + "\n" + f"Товар: {name_text}, Количество: {amount}"

            # new_text+="\n"+ f"Итого: {self.final_price}"
            if name_text in self.basket:
                self.basket[name_text] += int(amount)
            else:
                if name_text not in self.basket:
                    self.basket[name_text] = int(amount)

            self.plainTextEdit.setPlainText(new_text)
            print(self.basket)

    def save_data_for_products(self):
        current_item = self.listWidget2.currentItem()
        if current_item is not None:
            self.name_text = current_item.text()
            self.show_input_data_dialog(self.name_text)
    def save_data_for_client(self):
        current_item3 = self.listWidget3.currentItem()
        if current_item3 is not None:
            self.name_text3 = current_item3.text()
            print(self.name_text3)


    def save_data_for_storage2(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        current_item2 = self.listWidget.currentItem()
        if current_item2 is not None:
            self.name_text2 = current_item2.text()
            print(self.name_text2)


            data = {
                "Склад №1": self.name_text,
                "Товар": self.name_text2,
                "Склад №2": self.sclad,
                "Работник":self.personal,
                "Дата": self.textEdit_5.toPlainText()
            }

            print(self.name_text3)
            self.date_delivery =self.textEdit_5.toPlainText()

            header = ["Склад №1", "Товар","Склад №2","Работник","Дата"]

            excel_file = os.path.join(desktop_path, f"move_data{self.date_delivery}.xlsx")
            wb = Workbook()
            ws = wb.active
            ws.append(header)
            row_data = [data[key] for key in header]
            ws.append(row_data)
            wb.save(excel_file)

    def save_data_for_storage(self):

        current_item3 = self.listWidget3.currentItem()
        if current_item3 is not None:
            self.sclad = current_item3.text()
            print(self.sclad)


    def save_data_for_personal(self):
        current_item4 = self.listWidget4.currentItem()
        if current_item4 is not None:
            self.personal = current_item4.text()
            print(self.personal)
    def load_data(self):
        self.listWidget.clear()
        data = self.my_db.select_all_from_db()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(list_item)


    def load_data_client(self):
        self.listWidget3.clear()
        data = self.my_db.select_all_from_client()
        for item in data:
            name = str(item[1])
            list_item = QtWidgets.QListWidgetItem(name)
            self.listWidget3.addItem(list_item)


    def save_data_products(self):
        data = self.my_db.select_client_id(self.name_text3)
        print(data)
        print(self.basket)
        print(self.date_delivery)
        print(self.name_text3)
        # self.my_db.inser_into_sell_operation(data,self.date_delivery,self.final_price,1,str(self.basket))
        self.my_db.inser_into_operation("Перемещение товара",self.name_text3,self.date_delivery)


        self.show_notification("Покупка совершена")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Перемещение товара "))
        self.label_3.setText(_translate("Dialog", "Cклад №1"))
        self.label_2.setText(_translate("Dialog", "Товар"))
        self.label_6.setText(_translate("Dialog", "Склад №2"))
        self.label_4.setText(_translate("Dialog", "Работник"))
        self.label_5.setText(_translate("Dialog", "Дата"))
        self.pushButton_7.setText(_translate("Dialog", "Очистить корзину"))
        self.pushButton_10.setText(_translate("Dialog", "Оформление"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Move_product()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
