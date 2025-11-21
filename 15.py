# Q15: Write a function that takes an ordered list of numbers and a number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
def list_length(input_list):
    count = 0
    for element in input_list:
        count = count + 1
    return count

def is_number_in_list(ordered_list, target):
    low = 0
    high = list_length(ordered_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if ordered_list[mid] == target:
            return True
        elif ordered_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

a = [1, 5, 8, 12, 16, 20, 25, 30]
check_num = 16
result = is_number_in_list(a, check_num)
print(f"Is {check_num} in the list? {result}")