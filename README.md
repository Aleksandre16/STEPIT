# Python Apps Collection with PyQt5

This project includes a collection of **7 Python apps** developed using **PyQt5** for the graphical user interface (GUI). These apps aim to demonstrate different functionalities ranging from a simple calculator to a book management system. The apps are as follows:

1. **Calculator**: A simple calculator that performs basic arithmetic operations.
2. **Guess the Number**: A game where the user has to guess a randomly generated number.
3. **Hangman Game**: A word guessing game where users have to guess letters in a hidden word.
4. **Translator**: A dictionary-based translator app.
5. **ATM Simulator**: A simulation of an ATM machine that supports balance checking, deposits, and withdrawals.
6. **Book Management System**: A system to add, view, and search books by title.
7. **User System for ATM**: A modified ATM simulator that includes a basic user system with login functionality for users to access their balances securely.

## Features

- **Calculator**: Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
- **Guess the Number**: Generates a random number and asks the user to guess it.
- **Hangman Game**: A classic game where players guess letters in a word with a limited number of attempts.
- **Translator**: Translates words using a dictionary stored in a text file.
- **ATM Simulator**: Simulates the functionality of an ATM, including checking balance, depositing money, and withdrawing with a small fee.
- **Book Management**: Manages a collection of books with features for adding, searching by title, and displaying all books.
- **User System for ATM**: Includes login functionality and ensures that only logged-in users can access their ATM features.

## Installation

### Prerequisites

Ensure you have **Python 3.x** installed on your system. You will also need to install **PyQt5** for the GUI functionality.

### Steps to Install

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aleksandre16/STEPIT
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd STEPIT 
    ```

3. **Install Dependencies**:
    Install the required dependencies using pip:
    ```bash
    pip install PyQt5
    ```

### Running the Applications

1. After installing the dependencies, you can run any of the apps by executing the corresponding Python file:
    - **Calculator**:
      ```bash
      python calculator.py
      ```
    - **Guess the Number**:
      ```bash
      python guess_the_number.py
      ```
    - **Hangman Game**:
      ```bash
      python hangman.py
      ```
    - **Translator**:
      ```bash
      python translator.py
      ```
    - **ATM Simulator**:
      ```bash
      python atm_simulator.py
      ```
    - **Book Management System**:
      ```bash
      python book_management.py
      ```
    - **User System for ATM**:
      ```bash
      python atm_user_system.py
      ```

2. The corresponding app window will open, and you can interact with the app through the GUI.

## Application Details

### 1. Calculator

- **Description**: This app allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) with input validation.
- **Usage**: Enter the numbers and select the operation, then click "Calculate" to see the result.

### 2. Guess the Number

- **Description**: The app generates a random number between a specified range, and the user has to guess the number.
- **Usage**: Enter your guess in the text box and press "Guess" to see if you’re correct.

### 3. Hangman Game

- **Description**: A word guessing game where users have to guess the hidden word by entering letters.
- **Usage**: Type a letter to guess and keep track of the remaining attempts.

### 4. Translator

- **Description**: A translation app that uses a dictionary stored in a text file to translate words.
- **Usage**: Enter a word to translate and press "Translate."

### 5. ATM Simulator

- **Description**: Simulates an ATM where users can check their balance, make deposits, and withdraw money (with a withdrawal fee).
- **Usage**: Enter the amount to deposit or withdraw, and check your balance in the system.

### 6. Book Management System

- **Description**: A system to manage books, including adding, viewing, and searching books by title. The data is saved to a JSON file.
- **Usage**: Enter the title, author, and year of publication to add a book, or search for books by title.

### 7. User System for ATM

- **Description**: An enhancement to the ATM simulator, adding a user login system to ensure only logged-in users can access their ATM functions.
- **Usage**: Create an account with a username and password, log in to access ATM functionalities.

## Data Storage

Each app that requires data persistence stores its data in files. For example:
- **Books** are stored in a `books.json` file.
- **ATM balances** and **user data** can be stored in text files for consistency.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.
