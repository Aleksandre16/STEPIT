import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

# წიგნის კლასი
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, წელი: {self.year}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])

# წიგნების მართვის კლასი
class BookManager:
    def __init__(self, file_path="books.json"):
        self.books = []
        self.file_path = file_path
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def show_books(self):
        return "\n".join(str(book) for book in self.books)

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            return "\n".join(str(book) for book in found_books)
        else:
            return f"წიგნი(ები) ვერ მოიძებნა სათაურით: {title}"

    def save_books(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False)

    def load_books(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                book_dicts = json.load(file)
                self.books = [Book.from_dict(book) for book in book_dicts]
        except FileNotFoundError:
            self.books = []

# მთავარი ფანჯარა წიგნების მართვისთვის
class BookManagementWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("წიგნების მართვის სისტემა")
        self.setGeometry(200, 200, 400, 300)

        self.book_manager = BookManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("შეიყვანეთ წიგნის სათაური")
        layout.addWidget(self.title_input)

        self.author_input = QLineEdit(self)
        self.author_input.setPlaceholderText("შეიყვანეთ ავტორი")
        layout.addWidget(self.author_input)

        self.year_input = QLineEdit(self)
        self.year_input.setPlaceholderText("გამოშვების წელი")
        layout.addWidget(self.year_input)

        self.add_book_btn = QPushButton("წიგნის დამატება", self)
        self.add_book_btn.clicked.connect(self.add_book)
        layout.addWidget(self.add_book_btn)

        self.show_books_btn = QPushButton("ყველა წიგნის ნახვა", self)
        self.show_books_btn.clicked.connect(self.show_books)
        layout.addWidget(self.show_books_btn)

        self.search_btn = QPushButton("ძებნა სათაურით", self)
        self.search_btn.clicked.connect(self.search_books)
        layout.addWidget(self.search_btn)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        year = self.year_input.text()

        if not title or not author or not year:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ შეავსოთ ყველა ველი.")
            return

        try:
            year = int(year)
            book = Book(title, author, year)
            self.book_manager.add_book(book)
            QMessageBox.information(self, "წარმატება", "წიგნი დაემატა წარმატებით!")
            self.clear_inputs()
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ შეიყვანოთ ვალიდური წელი.")

    def show_books(self):
        books = self.book_manager.show_books()
        if not books:
            self.result_label.setText("წიგნები არ არსებობს.")
        else:
            self.result_label.setText(books)

    def search_books(self):
        search_title = self.title_input.text()
        result = self.book_manager.search_by_title(search_title)
        self.result_label.setText(result)

    def clear_inputs(self):
        self.title_input.clear()
        self.author_input.clear()
        self.year_input.clear()
