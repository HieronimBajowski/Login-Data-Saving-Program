from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QApplication, QMessageBox
from PySide6.QtGui import QCloseEvent

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()

        self.web_line_edit = QLineEdit("Web/app name", self)
        self.web_line_edit.move(170,70)

        self.login_line_edit = QLineEdit("Login", self)
        self.login_line_edit.move(170, 100)

        self.password_line_edit = QLineEdit("Password", self)
        self.password_line_edit.move(170, 130)

        self.submit_button = QPushButton("Save", self)
        self.submit_button.move(200, 160)
        self.submit_button.clicked.connect(self.save_password)

        self.find_line_edit = QLineEdit("Find", self)
        self.find_line_edit.move(170, 240)

        self.find_button = QPushButton("Find", self)
        self.find_button.move(200, 270)
        self.find_button.clicked.connect(self.find_password)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 310, 400, 200)

        layout = QVBoxLayout(self)
        layout.addWidget(self.web_line_edit)
        layout.addWidget(self.login_line_edit)
        layout.addWidget(self.password_line_edit)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.find_line_edit)
        layout.addWidget(self.find_button)
        layout.addWidget(self.text_edit)

        self.setWindowTitle("Password Manager")
        self.setGeometry(200, 200, 500, 550)
        self.show()

    def save_password(self):
        web = self.web_line_edit.text()
        login = self.login_line_edit.text()
        password = self.password_line_edit.text()

        with open('file.txt', 'a') as f:
            f.write(f'{web}, {login}, {password}\n')

        self.web_line_edit.clear()
        self.login_line_edit.clear()
        self.password_line_edit.clear()

    def find_password(self):
        search_term = self.find_line_edit.text()

        with open('file.txt', 'r') as f:
            data = f.readlines()

        results = []
        for line in data:
            if search_term in line:
                results.append(line.strip())

        if results:
            self.text_edit.setText('\n'.join(results))
        else:
            self.text_edit.setText(f'No results found for {search_term}')



    def closeEvent(self, event: QCloseEvent):
        close = QMessageBox.question(self, "Close app", "Do you want to close",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore

if __name__ == '__main__':
    app = QApplication([])
    pm = PasswordManager()
    app.exec_()
