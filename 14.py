# Q14: Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def remove_duplicates(input_list):
    new_list = []
    
    for item in input_list:
        is_duplicate = 0
        for unique_item in new_list:
            if item == unique_item:
                is_duplicate = 1
                break
        
        if is_duplicate == 0:
            new_list = new_list + [item]
            
    return new_list

a = [1, 1, 2, 3, 5, 8, 5, 13, 21, 3, 34, 55, 89]
unique_list = remove_duplicates(a)

print(f"List without duplicates: {unique_list}")