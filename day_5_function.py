#1st way. declaring all the thing inside the function

# sum of two num
# def sum():
#     a=int(input("enter first"))
#     b=int(input("enter first"))
#     print("sum: ",a+b)
    
# sum()

# factorial 
'''
def factorial():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Enter a positive number.")
    elif num==1:
        print("factorial is 1")  
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("factorial is:",fact)

factorial() ''' 

#2nd way. declaring the input outside the function

# sum of two num
# def sum(a,b):
#     print("sum: ",a+b)
# a=int(input("enter first"))
# b=int(input("enter first"))

# sum(a,b)

# swap
'''
def swap(a,b):                       
    temp = a
    a = b
    b = temp
    print(a,b)

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
swap(a,b) ''' 

# 3rd way
''' 
def power(a,b):
    c = a ** b
    return c

a = int(input("Enter 1st: "))
b = int(input("Enter 2nd : "))

c = power(a, b)
print(c)
'''

# arbitary / variable length argument--- any number of agrument we pass -- use * operator

def sum(*x):
    print(x)
    
a=int(input("enter first"))
b=int(input("enter second"))

sum()
sum(a)
sum(b)
sum(a,b)
sum(1,2,3,4) 


