from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class ConfirmationDialog(QDialog):
    def __init__(self):
        super(ConfirmationDialog, self).__init__()

        self.setWindowTitle("Подтверждение удаления")

        layout = QVBoxLayout(self)

        label = QLabel("Вы уверены, что хотите удалить выбранную запись?")
        layout.addWidget(label)

        self.confirm_button = QPushButton("Удалить", self)
        self.cancel_button = QPushButton("Отмена", self)

        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)

        self.confirm_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)