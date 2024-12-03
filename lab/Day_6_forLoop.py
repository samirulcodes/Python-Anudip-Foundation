# 1. Print the first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)  # o/p --> 1 to 10 exclude 11

# 2. Python program to check if the given string is a palindrome

str = input("Enter a string: ")
is_palindrome = True  # assuming is_palindrome is  true

for i in range(len(str) // 2):
    if str[i] != str[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"The string {str} is a palindrome")  # input - radar , o/p - palindrome
else:
    print(f"The string {str} is not a palindrome")  # input - rodent , o/p - not palindrome
    

# 3. Python program to check if a given number is an Armstrong number
Armstrong_number = int(input("Enter a number: "))
num = Armstrong_number
digit= 0
Armstrong_sum = 0

length = len(str(num))
for i in range(length):
    digit = num % 10
    num = num // 10
    Armstrong_sum += pow(digit, length)

if Armstrong_sum == Armstrong_number:
    print(f"{Armstrong_number} is an Armstrong number")
else:
    print(f"{Armstrong_number} is an Armstrong number")
    
    
# 4. Python program to get the Fibonacci series between 0 to 50
a = 0
b = 1
print(a) # printing value for a
print(b) # printing value for b---- so , 0,1,1----

for i in range(2, 10):
    temp = a + b
    if temp > 50:
        break
    print(temp)  # o/p-- 0,1,1,2,3,5,8,13,21,34 and not print (34+21) because it is greater than 50 and it meet the condition so it break & exit from the loop
    a, b = b, temp


# 5. Python program to check the validity of password input by users

# Input password
password = input("Enter your password: ")

# Initialize validation as false
is_upper = False
is_lower = False
is_digit = False
is_special = False
is_space = False

# Check each character in the password
for char in password:
    if char.isupper():
        is_upper = True
    elif char.islower():
        is_lower = True
    elif char.isdigit():
        is_digit = True
    elif char in "!@#$%^&*(),.?\":{}|<>":
        is_special = True
    elif char == " ":
        has_space = True

# Validate password
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not is_upper:
    print("Password must contain at least one uppercase letter.")
elif not is_lower:
    print("Password must contain at least one lowercase letter.")
elif not is_digit:
    print("Password must contain at least one number.")
elif not is_special:
    print("Password must contain at least one special character.")
elif is_space:
    print("Password must not contain spaces.")
else:
    print("Password is valid!")

