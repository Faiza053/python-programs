# Q9: Take two lists, say for example these two: a and b, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements_list = []

for item_a in a:
    is_in_b = 0
    for item_b in b:
        if item_a == item_b:
            is_in_b = 1
            break
            
    is_duplicate = 0
    if is_in_b == 1:
        for common in common_elements_list:
            if item_a == common:
                is_duplicate = 1
                break
                
        if is_duplicate == 0:
            common_elements_list = common_elements_list + [item_a]

print(f"Common elements (no duplicates): {common_elements_list}")