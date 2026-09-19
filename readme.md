# 🎯 Number Guessing Game

A simple **Number Guessing Game** made using Python.

The computer randomly selects a number between **1 and 100**, and the player has to guess the number. After every guess, the program gives a hint whether the guessed number is **too high** or **too low**.

## 📌 Features

* Generates a random number between 1 and 100
* Takes guesses from the user
* Gives hints after every incorrect guess
* Counts the number of attempts
* Handles invalid input
* Allows the player to play again
* Uses a different random number for every new game

## 🛠️ Technologies Used

* **Python**
* `random` module

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### 2. Open the Project

Open the project folder in **VS Code**.

### 3. Run the Program

Open the terminal in VS Code and type:

```bash
python number_guessing_game.py
```

## 🎮 How to Play

1. The computer selects a random number from **1 to 100**.
2. Enter your guess.
3. The program will tell you:

   * **Too low** → Try a bigger number.
   * **Too high** → Try a smaller number.
   * **Correct** → You win!
4. The program shows how many attempts you used.
5. You can choose whether to play again.

## 💻 Example

```text
==============================
      NUMBER GUESSING GAME
==============================

I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try a smaller number.

Enter your guess: 25
Too low! Try a bigger number.

Enter your guess: 37

🎉 Congratulations!
You guessed the number correctly!
Number of attempts: 3

Do you want to play again? (yes/no): yes
```

## 📚 Python Concepts Used

This project helped me practice:

* Variables
* Functions
* `while` loops
* `if`, `elif`, and `else`
* User input
* Exception handling
* `random` module
* Basic program logic

## 🚀 Future Improvements

Some features that could be added later:

* Difficulty levels
* Maximum number of att
