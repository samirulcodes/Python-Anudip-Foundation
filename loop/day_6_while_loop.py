#  1.      Print the reverse order series  using a while loop
# n = int(input("Enter a number: "))

# while n > 0:
#     print(n)
#     n -= 1

# 2.      Create a code that describe the use of break statement in while loop

# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# 3.      Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.
# string = "Python"
# index = 0

# while index < len(string):
#     print(string[index])
#     index += 1

# print("Length of the string:", len(string))

# 4.      Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.
num = int(input("Enter an integer: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("The factorial of", num, "is", factorial)