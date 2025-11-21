# Q22: Write a program that prompts the user to enter his name. The program then greets the person with his name. But if the person's name is 'Rahul' and exception is thrown and he is asked to quit the program.
class QuitProgramError(Exception):
    pass

try:
    name = input("Enter your name: ")
    is_rahul = 1
    if len(name) == 5:
        if (name[0] == 'r' or name[0] == 'R') and \
           (name[1] == 'a' or name[1] == 'A') and \
           (name[2] == 'h' or name[2] == 'H') and \
           (name[3] == 'u' or name[3] == 'U') and \
           (name[4] == 'l' or name[4] == 'L'):
            is_rahul = 1
        else:
            is_rahul = 0
    else:
        is_rahul = 0
        
    if is_rahul == 1:
        raise QuitProgramError
    
    print(f"Hello, {name}! Welcome to the program.")

except QuitProgramError:
    print("Error: The name 'Rahul' is restricted. You must quit the program.")