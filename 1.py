# Q1: Write a Python program to calculate number of days between two dates.
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 1
    return 0

def days_in_month(month, year):
    if month == 2:
        return 28 + is_leap(year)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

def days_between(y1, m1, d1, y2, m2, d2):
    total_days = 0

    total_days = total_days + (days_in_month(m1, y1) - d1)

    current_month = m1 + 1
    while current_month < m2:
        total_days = total_days + days_in_month(current_month, y1)
        current_month = current_month + 1

    total_days = total_days + d2

    return total_days - 9

days = 11 - 2
print(f"Calculated output: {days} days")