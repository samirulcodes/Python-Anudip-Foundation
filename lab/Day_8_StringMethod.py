# 1.WAP to Count all letters, digits, and special symbols from the given string:
# string = "P@#yn26at^&i5ve"

string = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

# iterate through each character in the string.
for char in string:
    if char.isalpha():
        chars += 1  #If the character is an alphabet, then increment the chars count.
    elif char.isdigit():
        digits += 1  # If the character is a digit, then increment the digits count.
    else:
        symbols += 1  # else increment symbol increment

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)

# output -  # Chars = 8
            # Digits = 3
            # Symbols = 4
            
            
# Q2.WAP to Remove duplicate characters of a given string:
# string = "String and String Function"

string = "String and String Function"
#  creating an empty string result to store characters.
result = ""
for char in string:  # iterate through each character in the string.
    if char not in result: # If the character is not already in the result string, we append it.
        result += char

print(result)

# output -- String adFuco


# Q3.WAP to Count Uppercase, Lowercase, special character, and numeric values in a given string:
# string = "Hello World! 123* # welcome to pYtHoN"

string = "Hello World! 123* # welcome to pYtHoN"

upper_case = 0
lower_case = 0
digits = 0
symbols = 0

# iterate through each character and check using isupper(), islower(), isdigit(), and else for symbols.

for char in string:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print("UpperCase:", upper_case)
print("LowerCase:", lower_case)
print("NumberCase:", digits)
print("SpecialCase:", symbols)

#output   # UpperCase: 5
          # LowerCase: 20
          # NumberCase: 3
          # SpecialCase: 9
        
        
# Q4.WAP to Count vowels in a string:
# string = "Welcome to Python Assignment"

string = "Welcome to Python Assignment"

# defining vowels
vowels = "aeiouAEIOU"
# Initializing vowel count to 0
vowel_count = 0

# # Iterate through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels in: {string} is: {vowel_count}")

# Output -- Number of vowels in: Welcome to Python Assignment is: 8