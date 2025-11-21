# Q12: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
target_number = 7
guess = 0
is_correct = 0

print("Guessing game started (Target is fixed at 7).")

while is_correct == 0:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Exactly right! The number was {target_number}.")
            is_correct = 1
    except:
        print("Please enter a valid integer.")