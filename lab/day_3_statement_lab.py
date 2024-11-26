# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
num = int(input("Enter a number: "))
n = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {n}.")


# 2. Using input function take two number and then swap the number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping {num1} {num2}")

# Swapping
temp = num1
num1 = num2
num2 = temp

print(f"After swapping {num1} {num2}")


# 3. Write a Program to Convert Kilometers to Miles
kilometers = float(input("Enter kilometers: "))

# 1 km = 0.621371 miles
one_km = 0.621371

# Calculating miles
miles = kilometers * one_km 

print(f"{kilometers} kilometers is equal to {miles} miles.")

#  4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
principal = 200
time = 5
rate = 5

simple_interest = (principal * time * rate) / 100

print("Simple interest is:", simple_interest)
