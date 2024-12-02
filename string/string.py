# string = input("Enter a string: ")
# vowels = "HelloUser"
# vowels = "aeiouAEIOU"
# count = 0

# for char in string:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)


# palindrome or not
# str = input("Enter a string: ")

# if str == str[::-1]:
#     print("The is a palindrome.")
# else:
#     print("not a palindrome.")
    

str = input("Enter a string: ")

letters = 0
digits = 0
specialChar = 0

for char in str:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        specialChar  += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", specialChar)
    
