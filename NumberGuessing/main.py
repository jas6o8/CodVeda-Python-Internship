import random

number = random.randint(1, 100)
guess = None
guess_count = 0

while guess != number and guess_count < 10:
    guess = int(input("Guess a number between 1 and 100, you have 10 guesses: "))
    guess_count += 1
    if guess < number:
        print("Too low!")
        print(f"You have {10 - guess_count} guesses left.")
    elif guess > number:
        print("Too high!")
        print(f"You have {10 - guess_count} guesses left.")
    elif guess_count == 10:
        print(f"Sorry, you've used all your guesses. The number was {number}.")
        break
    else:
        print("Congratulations! You guessed the number.")