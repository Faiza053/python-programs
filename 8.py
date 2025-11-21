# Q8: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num_input = input("Enter an integer to find its divisors: ")
num = int(num_input)
divisors = []
i = 1

while i <= num:
    if num % i == 0:
        divisors = divisors + [i]
    i = i + 1

print(f"The divisors of {num} are: {divisors}")