# class abc:
#     c=3  # global variable
#     d=5
#     def display(self,a,b):  # atleast one argument we have to pass
#         print("display",a+b)

# # object
# obj=abc()
# obj.display(2,4)
# print(obj.c)  # acccesing global var


# wap to print sum sub mul div rem of two number oops in python

# class ABC :
#     def sum(self,a,b):
#         print("SUM IS :", a+b)
#     def sub(self,a,b):
#         print("SUB IS :", a-b)
#     def mul(self,a,b):
#         print("MUL IS :", a*b)
#     def div(self,a,b):
#         print("DIV IS :", a/b)
#     def rem(self,a,b):
#         print("REM IS :", a%b)

# obj = ABC()
# obj.sum(6,7)
# obj.sub(6,7)
# obj.mul(6,7)
# obj.div(6,7)
# obj.rem(6,7)


# ANOTHER METHOD
# class calculation:
#     def init(self):
#         self.num1 = int(input("Enter num1: "))
#         self.num2 = int(input("Enter num2: "))
#     def add(self):
#         print("Addition is:",self.num1 + self.num2)
#     def sub(self):
#         print("Substraction is:",self.num1 - self.num2)
#     def mul(self):
#         print("Multiplication is:",self.num1 * self.num2)
#     def div(self):
#         print("Divition is:",self.num1 / self.num2)
#     def rem(self):
#         print("Remainder is:",self.num1 % self.num2)
        

# obj = calculation()
# obj.init()
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()
# obj.rem()

# eg - 1
# class A:
#     def __init__(self):
#         print("A constructor")

# class B(A):
#     def __init__(self):
#          print("B constructor")

# obj=B()  #o/p -- B constructor

# eg -2
class A:
    def init(self):
        print("A constructor")

class B():
    def init(self):
         print("B constructor")

obj=A() 
obj.init()   #o/p -- A constructor
