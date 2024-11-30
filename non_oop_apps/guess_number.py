import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import sys

# თამაში: "გამოიცანი რიცხვი"
class GuessNumberWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("გამოიცანი რიცხვი")
        self.setGeometry(100, 100, 300, 200)

        self.target_number = random.randint(1, 100)
        self.remaining_attempts = 10  # მცდელობების რაოდენობა

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("გამოიცანით რიცხვი 1-დან 100-მდე:")
        self.layout.addWidget(self.info_label)

        self.attempts_label = QLabel(f"დარჩენილი მცდელობები: {self.remaining_attempts}")
        self.layout.addWidget(self.attempts_label)

        self.input_guess = QLineEdit()
        self.input_guess.setPlaceholderText("შეიყვანეთ თქვენი ვარიანტი")
        self.layout.addWidget(self.input_guess)

        self.submit_button = QPushButton("შედგენა")
        self.submit_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.submit_button)

        self.central_widget.setLayout(self.layout)

    # მომხმარებლის მიერ მითითებული რიცხვის შემოწმება
    def check_guess(self):
        try:
            guess = int(self.input_guess.text())
            if guess < self.target_number:
                QMessageBox.information(self, "პასუხი", "თქვენი რიცხვი მცირეა.")
            elif guess > self.target_number:
                QMessageBox.information(self, "პასუხი", "თქვენი რიცხვი დიდიია.")
            else:
                QMessageBox.information(self, "გილოცავთ!", "თქვენ სწორად გამოიცანით!")
                self.reset_game()
                return

            self.remaining_attempts -= 1
            self.attempts_label.setText(f"დარჩენილი მცდელობები: {self.remaining_attempts}")

            if self.remaining_attempts == 0:
                QMessageBox.warning(self, "წაგება!", f"თქვენ წააგეთ! რიცხვი იყო: {self.target_number}")
                self.reset_game()
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანეთ ვალიდური რიცხვი.")

    # თამაშის განახლება
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.remaining_attempts = 10
        self.attempts_label.setText(f"დარჩენილი მცდელობები: {self.remaining_attempts}")
        self.input_guess.clear()
