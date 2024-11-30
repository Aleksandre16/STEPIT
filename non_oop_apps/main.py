import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from calculator import CalculatorWindow
from guess_number import GuessNumberWindow
from hangman import HangmanWindow
from translator import TranslatorWindow
from atm import ATMWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.calculator_btn = QPushButton("Calculator")
        self.calculator_btn.clicked.connect(self.open_calculator)
        layout.addWidget(self.calculator_btn)

        self.guess_number_btn = QPushButton("Guess the Number")
        self.guess_number_btn.clicked.connect(self.open_guess_number)
        layout.addWidget(self.guess_number_btn)

        self.hangman_btn = QPushButton("Hangman")
        self.hangman_btn.clicked.connect(self.open_hangman)
        layout.addWidget(self.hangman_btn)

        self.translator_btn = QPushButton("Translator")
        self.translator_btn.clicked.connect(self.open_translator)
        layout.addWidget(self.translator_btn)

        self.atm_btn = QPushButton("ATM")
        self.atm_btn.clicked.connect(self.open_atm)
        layout.addWidget(self.atm_btn)

        central_widget.setLayout(layout)

    def open_calculator(self):
        self.calculator_window = CalculatorWindow()
        self.calculator_window.show()

    def open_guess_number(self):
        self.guess_number_window = GuessNumberWindow()
        self.guess_number_window.show()

    def open_hangman(self):
        self.hangman_window = HangmanWindow()
        self.hangman_window.show()

    def open_translator(self):
        self.translator_window = TranslatorWindow()
        self.translator_window.show()

    def open_atm(self):
        self.atm_window = ATMWindow()
        self.atm_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
