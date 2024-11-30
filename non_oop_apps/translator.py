import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QInputDialog
import os


class TranslatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator")
        self.setGeometry(200, 200, 400, 300)

        self.translations = {}
        self.load_translations()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText("Enter word to translate")
        layout.addWidget(self.word_input)

        self.translate_btn = QPushButton("Translate")
        self.translate_btn.clicked.connect(self.translate_word)
        layout.addWidget(self.translate_btn)

        self.translation_label = QLabel("Translation will appear here")
        layout.addWidget(self.translation_label)

        self.setLayout(layout)

    def load_translations(self):
        file_path = "/Users/aleksandre/Desktop/Projects/pyproject/non_oop_apps/db/dictionary.txt"

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    if "=" in line:
                        # Split  (word=translation)
                        key, value = line.strip().split("=")
                        self.translations[key.strip().lower()] = value.strip()  # English -> Georgian
                        self.translations[value.strip().lower()] = key.strip()  # Georgian -> English
        else:
            QMessageBox.warning(self, "File Not Found", f"Dictionary file not found: {file_path}")

    def save_translations(self):
        with open("db/dictionary.txt", "w", encoding="utf-8") as file:
            for key, value in self.translations.items():
                file.write(f"{key}={value}\n")

    def translate_word(self):
        word = self.word_input.text().strip().lower()

        if not word:
            QMessageBox.warning(self, "Input Error", "Please enter a word to translate.")
            return

        translated_word = self.translations.get(word)

        if translated_word:
            self.translation_label.setText(f"Translation: {translated_word}")
        else:
            QMessageBox.warning(self, "Translation Error", "Translation not found. Would you like to add it?")
            self.add_new_translation(word)

    def add_new_translation(self, word):
        text, ok = QInputDialog.getText(self, "Add New Translation", f"Enter translation for '{word}':")

        if ok and text.strip():
            self.translations[word] = text.strip()
            self.translations[text.strip().lower()] = word  # Reverse translation (Georgian -> English)
            self.save_translations()  # Save updated dictionary to file
            QMessageBox.information(self, "Translation Added", "The new translation has been added successfully!")
            self.translation_label.setText(f"Translation: {text.strip()}")
        else:
            QMessageBox.warning(self, "Input Error", "No translation provided.")

