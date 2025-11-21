# Q3: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
try:
    num = int(input("Enter an integer: "))

    if (num % 2) == 0:
        print(f"The number is Even.")
    else:
        print(f"The number is Odd.")

except:
    print("Invalid input.")