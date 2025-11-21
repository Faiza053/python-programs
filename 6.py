# Q6: Write a Python program to test whether a passed letter is a vowel or not.
letter = input("Enter a single letter: ")
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
length_is_one = 0

i = 0
for char in letter:
    length_is_one = length_is_one + 1

if length_is_one == 1:
    is_alpha = 0
    if 'A' <= letter[0] <= 'Z' or 'a' <= letter[0] <= 'z':
        is_alpha = 1

    if is_alpha == 1:
        is_vowel = 0
        for v in vowels:
            if letter == v:
                is_vowel = 1
                break
        
        if is_vowel == 1:
            print(f"The letter is a Vowel.")
        else:
            print(f"The letter is a Consonant.")
    else:
        print("Invalid input.")
else:
    print("Invalid input.")