# Example - 1 


# a=input("Enter Number: ")
# print(f"Multiplication Table of {a} is ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")

# except:
#     print("Invalid Input")    

# print("Some important code")
# print("Heyy ! How are you")
    

# Example - 2 

# try:
#     num=int(input("Enter num "))
#     print(num**2)

# except ValueError:
#     print("Value Error , enter an integer")

# Example - 3 , multiple error can handeled

# try:
#     num=int(input("Enter num "))
#     # print(num**2)
#     a=[2,4] 
#     print(a[num])

# except ValueError:
#     print("Value Error , enter an integer")

# except IndexError:
#     print("Index Error , enter valid index number")
    
    
# Example - 4

# try:
#   # x=int(input("Enter num "))
#   print(x)        # throws an error(Name Error) , line 48 will execute because x is not defined
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  
  
# Example - 5

# try:
#   print("Hello")
#   # print(Hello)    # throws an error , in this case line 57 will execute
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# ANUDIP FOUNDATION 
# try:
#   a=100
#   b=0
#   print("hii")
#   c=a/b
#   print(c)
# except:
#   print("hello")


