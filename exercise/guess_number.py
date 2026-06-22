import random


random_num = random.randint(1,100)
guess = 0
guess_count = 0
while guess != random_num:
    guess = int(input("Guess a number between 1 and 100: "))
    guess_count += 1
    if guess < random_num:
        print("Too low! Try again.")
    elif guess > random_num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        print(f"It took you {guess_count} guesses.")