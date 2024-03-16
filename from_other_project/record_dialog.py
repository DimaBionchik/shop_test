from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton


class AddRecordDialog(QDialog):
    def __init__(self, field_names):
        super(AddRecordDialog, self).__init__()

        self.setWindowTitle("Добавить запись")

        self.layout = QFormLayout(self)
        self.line_edits = []

        for field_name in field_names:
            # Пропускаем поле id
            if field_name.lower() == 'id':
                continue

            line_edit = QLineEdit(self)
            self.line_edits.append(line_edit)
            self.layout.addRow(QLabel(f"{field_name}:"), line_edit)

        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.accept)

        self.layout.addRow(self.add_button)

    def get_data(self):
        return [line_edit.text() for line_edit in self.line_edits]