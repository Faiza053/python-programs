# Q4: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
data = input("Enter comma-separated numbers (e.g., 1, 2, 3, 4): ")
data_list = []
temp_number = ""

i = 0
while i < len(data):
    if data[i] != ',':
        temp_number = temp_number + data[i]
    else:
        data_list = data_list + [temp_number]
        temp_number = ""
    i = i + 1
data_list = data_list + [temp_number]

data_tuple = tuple(data_list)

print(f"List: {data_list}")
print(f"Tuple: {data_tuple}")