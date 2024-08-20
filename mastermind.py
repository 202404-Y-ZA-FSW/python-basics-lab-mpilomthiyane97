import random
random_number = (random.randint(1,100))
attempts = 0

while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if user_guess> random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")
    elif user_guess == random_number:
        print("correct!")
        print(f"attempts: {attempts}")
        break 