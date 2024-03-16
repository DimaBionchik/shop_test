
from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtWidgets import QDialog
from openpyxl import Workbook


class InnerDialog(QDialog):
    def __init__(self, parent=None):
        super(InnerDialog, self).__init__(parent)

        self.setWindowTitle("Внутреннее окно")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Продажа")
        self.label_2 = QtWidgets.QLabel(self)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_3.setText("Покупатель")
        self.label_2.setText("Продавец")
        self.label_5.setText("Товар")
        self.label_7.setText("Сумма")
        self.label_6.setText("Склад №")
        self.label_4.setText("Дата")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_7 = QtWidgets.QLineEdit(self)


        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.lineEdit_3)
        layout.addWidget(self.lineEdit_4)
        layout.addWidget(self.lineEdit_5)
        layout.addWidget(self.lineEdit_6)
        layout.addWidget(self.lineEdit_7)