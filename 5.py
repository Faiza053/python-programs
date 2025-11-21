# Q5: Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def calculate_sum(x, y, z):
    if x == y and y == z:
        return 3 * (x + y + z)
    else:
        return x + y + z

num1 = 5
num2 = 5
num3 = 5
print(f"Result: {calculate_sum(num1, num2, num3)}")

num4 = 1
num5 = 2
num6 = 3
print(f"Result: {calculate_sum(num4, num5, num6)}")