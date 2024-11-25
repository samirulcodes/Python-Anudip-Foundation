#operator practicing
'''
a=10
b=4
print(a/b)
print(-10/3)
print(5//2)
print(-5//2) #o/p: -3
print(-5.0//2)
print(4**2)
print(10!=10)
print(10>=10)
print(not(10==10)and (10<12))
print(a is not b)
print("a" in "aeiou")
'''

#avg
'''
num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50

sum = num1 + num2 + num3 + num4 + num5

average = sum / 5

print(average)
'''

#addition of 1 and last digit
'''
num = int(input("Enter a four-digit number: "))

a = num // 1000

b = num % 10

sum=a+b

print(sum)
'''

#greatest among two num
"""
x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))

c= x if x > y else y

print(c)
"""

#even or odd
'''
num = int(input("Enter a number: "))

a = "Even" if num % 2 == 0 else "Odd"

print(a)
'''

#number by day . if num==1 -> monday
'''
num = int(input("Enter a number: "))
if num==1:
    print("monday")

elif num==2:
    print("tuesday")
        

elif num==3:
    print("wednesday")

elif num==4:
    print("thursday")

elif num==5:
    print("friday")

elif num==6:
    print("saturday")

elif num==7:
    print("sunday")
else:
    print("Enter num b/w 1 to 7")

num = int(input("Enter a number: "))
'''


# greatest among 3 num
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
'''

# vowel or consonent

char = input("Enter a char: ")

if char in 'aeiouAEIOU':
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")




