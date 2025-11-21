# Q2: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n_str = input("Enter an integer (n): ")

n = int(n_str)
nn_str = n_str + n_str
nnn_str = n_str + n_str + n_str

nn = int(nn_str)
nnn = int(nnn_str)

result = n + nn + nnn

print(f"The value is: {result}")