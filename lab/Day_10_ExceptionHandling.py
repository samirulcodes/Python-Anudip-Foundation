# 1.WAP to Handling ZeroDivisionError exception when dividing a number by zero

# here use a try-except block to handle the error
try:
    # taking user input
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  #divide
    print("Result:", result)
except ZeroDivisionError:  # if user try to divide with 0 the except block will execute
    print("Error: Division by zero is not allowed.")

    
# 2. WAP to that prompts the user input an integer and raises a valueEror if the input is not a valid integer

# here use a try-except block to handle the error
try:
    # Taking user input 
    num = input("Enter an integer: ")
    
    # Check if the input is a valid integer
    if not num.isdigit():
        raise ValueError("Not a valid integer.")
    
    # Convert to integer
    num = int(num)
    print(f"The integer you entered is: {num}")

except ValueError as e:
    # Catch the ValueError and print the error message
    print(f"ValueError: {e}")


# 3.WAP that opens a file and Handle FileNotFoundError exception if the file does not exist

filename = input("Enter the filename: ") # asking to user to enter the file name

# here use a try-except block to handle the error
try:
    with open(filename, 'r') as file:  # if file exist the try block will execute
        print(file.read())  # read the text from the file
        
except FileNotFoundError:
    print("Error: File not found.") # if user enter wrong file name then except block will execute


# 4 WAP that prompts the user to input two number and raises a TypeError exception if the input are not numerical

# here use a try-except block to handle the error  
try:
    # Taking user input 
    num1 = input("Enter an integer: ")
    num2 = input("Enter an integer: ")
    
    # Check if the input is a valid integer
    if not num1.isdigit() or not num2.isdigit():
        raise TypeError("Both inputs must be numerical.") # if not numerical then raise TypeError
    
    # Convert to integer
    num1 = int(num1)
    num2 = int(num2)
    print(f"The integer you entered is: {num1} {num2}")

except TypeError as e:
    print(f"ValueError: {e}")  # if not numerical then provide TypeError: Both inputs must be numerical.