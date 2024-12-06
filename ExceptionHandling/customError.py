# Ex - 1

# num=int(input("Enter number between 3 and 8: "))

# if(num<3 or num>8):
#     raise ValueError("Value should be between 3 and 8")
    
# Ex - 2  (quick quiz) 
    
# num = str(input("Enter the value butween 3 and 8: "))

# if (num == "quit"):
#   print("ok")
# elif (int(num) < 3 or int(num) > 8):
#   raise ValueError("The number should be between 5 and 9")



# ANUDIP FOUNDATION
# class AgeNotValidException(Exception):   #mean-- AgeNotValidException extend Exception
#     def __init__(self,message):
#         self.message=message

# num = int(input("Enter your age "))
# try:
#     if num>18:
#         print("Age is valid")
#     else:
#         raise AgeNotValidException("Age is not Validate")
# except AgeNotValidException as e:
#     print(e.message)
        



# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except:
    raise ValueError("Invalid input. Please enter a valid integer.")