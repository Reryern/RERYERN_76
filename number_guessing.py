import random

lowest_num = 10
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num }")

while is_running:
    guess= input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Select a number between {lowest_num} and {highest_num }")
        elif highest_num == lowest_num:
            print("This is impossibe")
        
        elif guess < answer:
            print("too low! Try again")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num }")
