from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox
import sys

# კალკულატორის ფანჯრის კლასი
class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("კალკულატორი")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.result_label = QLabel("შედეგი: 0")
        self.layout.addWidget(self.result_label)

        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("შეიყვანეთ პირველი რიცხვი")
        self.layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("შეიყვანეთ მეორე რიცხვი")
        self.layout.addWidget(self.input2)

        self.add_button = QPushButton("დამატება (+)")
        self.add_button.clicked.connect(self.add_numbers)
        self.layout.addWidget(self.add_button)

        self.subtract_button = QPushButton("გამოკლება (-)")
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton("გამრავლება (*)")
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.layout.addWidget(self.multiply_button)

        self.divide_button = QPushButton("გაყოფა (/)")
        self.divide_button.clicked.connect(self.divide_numbers)
        self.layout.addWidget(self.divide_button)

        self.central_widget.setLayout(self.layout)

    # ორი რიცხვის დამატება
    def add_numbers(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 + num2
            self.result_label.setText(f"შედეგი: {result}")
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანეთ ვალიდური რიცხვები.")

    # ორი რიცხვის გამოკლება
    def subtract_numbers(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 - num2
            self.result_label.setText(f"შედეგი: {result}")
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანეთ ვალიდური რიცხვები.")

    # ორი რიცხვის გამრავლება
    def multiply_numbers(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 * num2
            self.result_label.setText(f"შედეგი: {result}")
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანეთ ვალიდური რიცხვები.")

    # ორი რიცხვის გაყოფა
    def divide_numbers(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            self.result_label.setText(f"შედეგი: {result}")
        except ZeroDivisionError:
            QMessageBox.warning(self, "შეცდომა", "ნული არ შეიძლება იყოს გამყოფი.")
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანეთ ვალიდური რიცხვები.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec_())
