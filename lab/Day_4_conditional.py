# 1. Check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# 2. Find the largest among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1>num2 and num1>num3:
    print(f"{num1} is largest")

elif num2>num1 and num2>num3:
    print(f"{num2} is largest")

else:
    print(f"{num3} is largest")


# 3. Check if a number is positive, negative or 0
num = float(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

# 4. Toy Vendor Discount
product_code = int(input("Enter the product code: "))
order_amount = float(input("Enter the order amount: "))
discount = 0
if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10
Total_amount = order_amount - (order_amount * discount)
print(f"Total_amount to paid is: {Total_amount}")

# 5. Transport Company Fare Calculation
distance = int(input("Enter the distance: "))
fare = 0
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = 50 * 8 + (distance - 50) * 10
else:
    fare = 50 * 8 + 50 * 10 + (distance - 100) * 12
print("Total fare:", fare)


# explanation of 5th question
# First 50 km:
# If the distance is less than or equal to 50 km, then fare is calculated by-- fare=(distance * 8/km) .

# Next 51 - 100 km:
# If the distance is between 51 km and 100 km, then:
# The fare for the first 50 km (50 * 8)
# and remaining distance (distance - 50) multiplied by 10 Rs/km.
# fare=50 * 8 + (distance - 50) * 10

# Over 100 km:
# If the distance is more than 100 km, then fare will be:
# The fare for the first 50 km (50 * 8)
# The fare for the next 50 km (50 * 10)
# The fare for the remaining distance (distance - 100) multiplied by 12 Rs/km.
# fare = 50 * 8 + 50 * 10 + (distance - 100) * 12