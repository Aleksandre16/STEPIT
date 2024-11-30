import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from book_management import BookManagementWindow
from student_management import StudentManagementWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.book_management_btn = QPushButton("Book Management System")
        self.book_management_btn.clicked.connect(self.open_book_management)
        layout.addWidget(self.book_management_btn)

        self.student_management_btn = QPushButton("Student Management System")
        self.student_management_btn.clicked.connect(self.open_student_management)
        layout.addWidget(self.student_management_btn)

        central_widget.setLayout(layout)

    def open_book_management(self):
        self.book_management_window = BookManagementWindow()
        self.book_management_window.show()

    def open_student_management(self):
        self.student_management_window = StudentManagementWindow()
        self.student_management_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
