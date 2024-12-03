# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division
def div(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print("Division:", result)

div(10, 5)  # Output: Division: 2.0

# 2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number.
def square(num):
    result = num * num
    print("Square:", result)

square(4)  # Output: Square: 16

# 3.Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random

#generate random num b/w 1 to 100 and generate 5 number
numbers = [random.randint(1, 100) for _ in range(5)] 
print("Random numbers:", numbers)

max_num = max(numbers)
min_num = min(numbers)

print("Maximum:", max_num)
print("Minimum:", min_num)


# 4.Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
lowerCase = name.lower()
print("Name in lowercase:", lowerCase)