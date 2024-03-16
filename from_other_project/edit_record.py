from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class EditRecordDialog(QDialog):
    def __init__(self, field_names, current_data):
        super(EditRecordDialog, self).__init__()

        self.setWindowTitle("Редактирование записи")

        layout = QVBoxLayout(self)

        self.input_fields = []

        for field_name, current_value in zip(field_names[1:], current_data[1:]):
            label = QLabel(f"{field_name}:")
            layout.addWidget(label)

            line_edit = QLineEdit(self)
            line_edit.setText(str(current_value))
            layout.addWidget(line_edit)

            self.input_fields.append(line_edit)

        self.save_button = QPushButton("Сохранить", self)
        self.cancel_button = QPushButton("Отмена", self)

        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_new_data(self):
        return [field.text() for field in self.input_fields]
