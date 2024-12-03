# 1. Reverse a Number Using a While Loop
num = int(input("Enter a number: ")) # taking user input
reverse = 0

while num > 0:
    digit = num % 10  #extract the last digit of number using (%).
    reverse = reverse * 10 + digit #
    num //= 10

print("Reversed number:", reverse)


# 2. Check if a Number is Palindrome
num = int(input("Enter a number: ")) # taking user input
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print(num, "is a palindrome") 
else:
    print(num, "is not a palindrome")
    

# 3. Find Factorial Using a While Loop
num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial of", num, "is", factorial)


# . Sum of Numbers Until 0
#  provide the number until you want like from  0 to 10,100,1000 etc and it provide output of all number of sum you enter

sum = 0
num = int(input("Enter a number until you want: "))

while num != 0:
    sum += num
    num = int(input("Enter a number until you want: "))

print("Sum of the numbers:", sum)

