# 🪓 **Project 4: Rock, Paper, Scissors** 🖐️

#### **Description**
This project implements the classic Rock, Paper, Scissors game where the user plays against the computer. The user inputs their choice, and the computer randomly selects one of the three options. The game then determines the winner based on the standard rules of the game.

---

#### **Code Overview**

```python
import random

def play():
    options = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in options:
        print("Invalid choice! Please select rock, paper, or scissors.")
        return play()

    computer_choice = random.choice(options)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

play()
```

---

#### **How It Works**

1. **User Input**: The user is asked to choose between "rock", "paper", or "scissors". The input is converted to lowercase to handle case insensitivity.
2. **Input Validation**: If the user's choice is invalid (not one of the three options), the program prints a message and asks the user to input their choice again.
3. **Computer Choice**: The computer randomly selects one of the three options using `random.choice()`.
4. **Comparison**: The program compares the user's choice and the computer's choice to determine the winner:
   - **Tie**: If both choices are the same, it's a tie.
   - **User Wins**: If the user’s choice beats the computer’s choice, the user wins.
   - **Computer Wins**: Otherwise, the computer wins.
5. **Replay**: The game doesn't automatically restart, but if needed, you could add a replay option by calling `play()` again after each round.

---

#### **Example Output**

```
Choose rock, paper, or scissors: paper
You chose: paper
Computer chose: scissors
Computer wins! 😢
```

---

#### **Why Is This Fun?**
🎮 **Interactive**: You play directly against the computer.  
🏆 **Challenge**: Try to outguess the computer's choices!  
💻 **Python Practice**: Practice using conditional statements, random choices, and user input validation.

---