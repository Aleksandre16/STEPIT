import sys
import os
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication


class ATMWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATM")
        self.setGeometry(200, 200, 400, 300)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_directory = os.path.join(base_dir, "db")
        os.makedirs(self.db_directory, exist_ok=True)
        self.file_name = os.path.join(self.db_directory, "users_data.json")

        self.user = None
        self.withdrawal_fee = 0.02
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Login section
        self.info_label = QLabel("გთხოვთ გაიარეთ ავტორიზაცია")
        layout.addWidget(self.info_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        self.register_btn = QPushButton("Register")
        self.register_btn.clicked.connect(self.register)
        layout.addWidget(self.register_btn)

        # Balance and transaction section
        self.balance_label = QLabel("")
        layout.addWidget(self.balance_label)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("შეიყვანეთ მნიშვნელობა")
        layout.addWidget(self.amount_input)

        self.deposit_btn = QPushButton("თანხის შეტანა")
        self.deposit_btn.clicked.connect(self.deposit_money)
        self.deposit_btn.setEnabled(False)
        layout.addWidget(self.deposit_btn)

        self.withdraw_btn = QPushButton("თანხის გამოტანა")
        self.withdraw_btn.clicked.connect(self.withdraw_money)
        self.withdraw_btn.setEnabled(False)
        layout.addWidget(self.withdraw_btn)

        self.setLayout(layout)

    def load_users(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self, users):
        with open(self.file_name, "w") as file:
            json.dump(users, file, indent=4)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "გთხოვთ შეიყვანოთ როგორც Password ასევე Username")
            return

        users = self.load_users()
        if username in users and users[username]["password"] == password:
            self.user = username
            self.info_label.setText(f"მოგესალმებით, {username}!")
            self.balance_label.setText(f"ბალანსი: {users[username]['balance']} ლარი")
            self.deposit_btn.setEnabled(True)
            self.withdraw_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "Login Error", "არასწორი Username ან Password")

    def register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "გთხოვთ შეიყვანოთ როგორც Password ასევე Username.")
            return

        users = self.load_users()
        if username in users:
            QMessageBox.warning(self, "Registration Error", "Username უკვე არსებობს.")
        else:
            users[username] = {"password": password, "balance": 0.0}
            self.save_users(users)
            QMessageBox.information(self, "Success", "User დარეგისტრირდა წარმატებით!")

    def get_balance(self):
        users = self.load_users()
        return users[self.user]["balance"]

    def update_balance(self, new_balance):
        users = self.load_users()
        users[self.user]["balance"] = new_balance
        self.save_users(users)

    def deposit_money(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("დადებითი რიცხვი შეიყვანეთ.")
            balance = self.get_balance() + amount
            self.update_balance(balance)
            self.balance_label.setText(f"ბალანსი: {balance} ლარი")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "გთხოვთ შეიყვანეთ ვალიდური დადებითი რიცხვი.")

    def withdraw_money(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("დადებითი რიცხვი უნდა იყოს")
            balance = self.get_balance()
            fee = amount * self.withdrawal_fee
            total_amount = amount + fee
            if total_amount > balance:
                raise ValueError("არასაკმარისი თანხა(საკომისიოს ჩათვლით).")
            balance -= total_amount
            self.update_balance(balance)
            self.balance_label.setText(f"ბალანსი: {balance} ლარი")
            QMessageBox.information(self, "ტრანზაქცია წარმატებულია", f"გამოტანილია: {amount} ლარი\nFee: {fee:.2f} ლარი")
        except ValueError as e:
            QMessageBox.warning(self, "Transaction Error", str(e))

