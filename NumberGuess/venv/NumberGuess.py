import random

answer: int = random.randint(1,100)
guess = 0

attempts = 0

highAttempts = 0
lowAttempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
while answer != guess:
    guess = int(input())
    if guess < answer:
        print(f"Sorry, {guess} is too low. Try again.")
        attempts += 1
        lowAttempts += 1
    elif guess > answer:
        print(f"Sorry, {guess} is too high. Try again.")
        attempts += 1
        highAttempts += 1
attempts += 1

print(f"Congratulations! It was {answer}!")
print(f"You guessed it in {attempts} attempts.")
print(f"Attempts too high = {highAttempts}")
print(f"Attempts too low = {lowAttempts}")

