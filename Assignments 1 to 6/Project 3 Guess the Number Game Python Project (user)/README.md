# 🎮 **Project 3: Guess the Number Game (User)** 🤔

#### **Description**  
In this project, the user attempts to guess a secret number that the computer randomly selects between 1 and 100. The program provides feedback on whether the guess is too high or too low until the user guesses the correct number. This project allows for practice with loops, conditionals, user input validation, and random number generation.

---

#### **Code Overview**

```python
import random

def guess_the_number():
    secret_number = random.randint(1, 100)  
    guess = 0

    print("I've chosen a number between 1 and 100. Can you guess it? 🤔")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            if guess < secret_number:
                print("Too low! Try again. 📉")
            elif guess > secret_number:
                print("Too high! Try again. 📈")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"🎉 Congratulations! You guessed the correct number: {secret_number} 🎯")

guess_the_number()
```

---

#### **How It Works**  
1. **Random Secret Number**: The program selects a random number between 1 and 100 as the "secret number".
2. **User Input**: The user is prompted to guess the number. The program checks the guess and provides feedback:
    - **Too low**: If the guess is lower than the secret number, the program will inform the user to try again with a higher guess.
    - **Too high**: If the guess is higher than the secret number, the program will inform the user to try again with a lower guess.
3. **Loop Until Correct**: The loop continues until the user guesses the correct number, at which point the program congratulates the user.
4. **Error Handling**: If the user inputs a non-numeric value, the program will catch the error and prompt them to enter a valid number.

---

#### **Example Output**

```
I've chosen a number between 1 and 100. Can you guess it? 🤔
Enter your guess: 50
Too low! Try again. 📉
Enter your guess: 75
Too high! Try again. 📈
Enter your guess: 60
Too low! Try again. 📉
Enter your guess: 65
🎉 Congratulations! You guessed the correct number: 65 🎯
```

---

#### **Why Is This Fun?**
🎯 **Challenge**: The user has to rely on the feedback to narrow down the range of possibilities.  
📈 **Interactive**: It involves interaction with the user, encouraging them to improve their guessing strategy.  
💻 **Python Practice**: It’s a great exercise for practicing loops, conditionals, and error handling in Python.

---