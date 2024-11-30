import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"სახელი: {self.name}, სიის ნომერი: {self.roll_number}, ქულა: {self.grade}"

    def to_dict(self):
        return {"name": self.name, "roll_number": self.roll_number, "grade": self.grade}

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(data["name"], data["roll_number"], data["grade"])
        except KeyError as e:
            print(f"Key error: {e} in data: {data}")
            return None


class StudentManager:
    def __init__(self, file_path="students.json"):
        self.students = []
        self.file_path = file_path
        self.load_students()

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def show_students(self):
        return "\n".join(str(student) for student in self.students)

    def search_by_roll_number(self, roll_number):
        found_students = [student for student in self.students if student.roll_number == roll_number]
        if found_students:
            return "\n".join(str(student) for student in found_students)
        else:
            return f"ამ სიის ნომრით სტუდენტი ვერ მოძებნა: {roll_number}"

    def update_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                self.save_students()
                return f"ქულა განახლდა: {student.name}. - სთვის"
        return f"სტუდენტი ამ სიის ნომრით: {roll_number} ვერ მოიძებნა."

    def save_students(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=4)

    def load_students(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                student_dicts = json.load(file)
                self.students = [Student.from_dict(student) for student in student_dicts if student is not None]
        except FileNotFoundError:
            self.students = []


class StudentManagementWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setGeometry(200, 200, 400, 300)

        self.student_manager = StudentManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("შეიყვანეთ სტუდენტის სახელი")
        layout.addWidget(self.name_input)

        self.roll_number_input = QLineEdit(self)
        self.roll_number_input.setPlaceholderText("შეიყვანეთ სტუდენტის სიის ნომერი")
        layout.addWidget(self.roll_number_input)

        self.grade_input = QLineEdit(self)
        self.grade_input.setPlaceholderText("შეიყვანეთ ქულა")
        layout.addWidget(self.grade_input)

        # Buttons for various actions
        self.add_student_btn = QPushButton("სტუდენტის დამატება", self)
        self.add_student_btn.clicked.connect(self.add_student)
        layout.addWidget(self.add_student_btn)

        self.show_students_btn = QPushButton("ყველა სტუდენტის ჩვენება", self)
        self.show_students_btn.clicked.connect(self.show_students)
        layout.addWidget(self.show_students_btn)

        self.search_btn = QPushButton("სტუდენტის მოძებნა (სიის ნომრით)", self)
        self.search_btn.clicked.connect(self.search_students)
        layout.addWidget(self.search_btn)

        self.update_grade_btn = QPushButton("ქულის განახლება", self)
        self.update_grade_btn.clicked.connect(self.update_grade)
        layout.addWidget(self.update_grade_btn)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def add_student(self):
        name = self.name_input.text()
        roll_number = self.roll_number_input.text()
        grade = self.grade_input.text()

        if not name or not roll_number or not grade:
            QMessageBox.warning(self, "Input Error", "გთხოვთ შეავსოთ ყველა ველი")
            return

        student = Student(name, roll_number, grade)
        self.student_manager.add_student(student)
        QMessageBox.information(self, "Success", "სტუდენტი დაემატა წარმატებით!")
        self.clear_inputs()

    def show_students(self):
        students = self.student_manager.show_students()
        if not students:
            self.result_label.setText("სტუდენტების სია ველი ცარიელია.")
        else:
            self.result_label.setText(students)

    def search_students(self):
        roll_number = self.roll_number_input.text()
        result = self.student_manager.search_by_roll_number(roll_number)
        self.result_label.setText(result)

    def update_grade(self):
        roll_number = self.roll_number_input.text()
        new_grade = self.grade_input.text()
        result = self.student_manager.update_grade(roll_number, new_grade)
        self.result_label.setText(result)

    def clear_inputs(self):
        self.name_input.clear()
        self.roll_number_input.clear()
        self.grade_input.clear()
