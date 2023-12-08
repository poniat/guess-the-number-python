import random
import os

numberOfTries = 0
found = False
numberToGuess = random.randint(0, 100)

os.system("cls")

while not found:
    numberOfTries += 1
    playerGuess = int(input(f"Guess the number (0-100): "))
    if playerGuess == numberToGuess:
        print(f"GAME OVER! You found {numberToGuess} in {numberOfTries} tries.")
        break
    elif playerGuess > numberToGuess:
        print(f"Your guess is too HIGH!")
    else:
        print(f"Your guess is too LOW!")