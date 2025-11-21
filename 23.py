# Q23: Write a program that accepts date of birth along with the other personal details. Throw an exception if an invalid date is entered.
def check_date_validity(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > 31:
        return False
    
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30: return False
    elif month == 2:
        if day > 29: return False
    return True

def get_personal_details():
    name = input("Enter name: ")
    
    while True:
        dob_str = input("Enter Date of Birth (YYYY-MM-DD): ")
        
        parts = dob_str.split('-')
        if len(parts) == 3:
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                
                if check_date_validity(year, month, day):
                    print("\nDetails successfully recorded.")
                    return
                else:
                    print("Invalid date value.")
            except:
                print("Invalid format.")
        else:
            print("Invalid format. Please use YYYY-MM-DD.")

get_personal_details()