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