#  1. Calculate the multiplication and sum of two numbers 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
product = num1 * num2

print("The sum of", num1, "and", num2, "is:", sum)
print("The product of", num1, "and", num2, "is:", product)



# 2. Declare two variables and print that which variable is largest using ternary operators
num1 = 10
num2 = 20

largest = num1 if num1 > num2 else num2

print("The largest number is:", largest)  



#  3. Python program to convert the temperature in degree centigrade to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees celsius in fahrenheit is {fahrenheit}")
print(celsius,"degrees celsius in fahrenheit is",fahrenheit)


#  4. Python program to find the area of a triangle whose sides are given
import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

#semi-perimeter
s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The area of the triangle is:", area)