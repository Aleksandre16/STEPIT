import sys
from random import choice
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QLineEdit, QWidget, QPushButton, QApplication


class HangmanWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hangman")
        self.setGeometry(200, 200, 400, 300)
        self.word_list = ["python", "hangman", "programming", "developer"]
        self.word = choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 6
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.word_label = QLabel(" ".join(self.guessed_word))
        layout.addWidget(self.word_label)

        self.letter_input = QLineEdit()
        self.letter_input.setPlaceholderText("გამოიცანი სიტყვა")
        layout.addWidget(self.letter_input)

        self.guess_btn = QPushButton("გამოიცანი")
        self.guess_btn.clicked.connect(self.guess_letter)
        layout.addWidget(self.guess_btn)

        self.result_label = QLabel(f"დაგრჩა ცდა: {self.attempts}")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def guess_letter(self):
        letter = self.letter_input.text().lower()
        if len(letter) != 1 or not letter.isalpha():
            QMessageBox.warning(self, "Input Error", "გთხოვთ შეიყვანოთ მხოლოდ ერთი ასო")
            return

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[i] = letter
            self.word_label.setText(" ".join(self.guessed_word))
        else:
            self.attempts -= 1

        self.result_label.setText(f"ცდების რაოდენობა: {self.attempts}")

        if "_" not in self.guessed_word:
            self.result_label.setText("შენ გამოიცანი სიტყვა!")
            QMessageBox.information(self, "გილოცავ", "შენ მოიგე თამაში!")
        elif self.attempts == 0:
            self.result_label.setText(f"თამაში დასრულდა! სიტყვა იყო: '{self.word}'.")
            QMessageBox.information(self, "თამაში დასრულდა", f"სიტყვა იყო: '{self.word}'.")
