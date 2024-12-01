# Q.1 print helloworld
print(" hello world")

#Q.2 describe local variable and global variable code

# Global variable
x = 10

if True:
    # Local variable
    y = 20 
    print("Inside block, Global variable x:", x)
    print("Inside block, Local variable y:", y)

# Accessing the global variable outside the block
print("Outside block, Global variable x:", x)

# Accessing the local variable outside the block
#print("Outside block, Local variable y:", y)
#x (global variable) is accessible both inside and outside the block.
#y (local variable) is only accessible inside the block where it is defined.



#Q.3 Write a code that describe Indentation error
#here is indentation error
'''
x = 10
if x > 5:
print("x is greater than 5")'''

# correct code
x = 10
if x > 5:
    print("x is greater than 5")
    

#Q.4 write a code that describe local and global variable with same name
# Global variable
x = 10

# Inside a block (like if)
if True:
    # Local variable with the same name
    x = 20
    print("Inside the block, Local variable x:", x)

# Outside the block, using the global variable
print("Outside the block, Global variable x:", x)

''' the global x has been updated to 20 because Python used the local assignment to modify the global variable, as there was no explicit global keyword. '''


    

#Q.5 Write a code for string, int and float input.

name = input("Enter your name: ")


age = int(input("Enter your age: "))


height = float(input("Enter your height (in meters): "))

print("Name:", name)
print("Age:", age)
print("Height:", height)

