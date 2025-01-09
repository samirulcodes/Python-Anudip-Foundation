# Q1: Find the number of times 4 appears in the tuple

# Create a tuple
tuple1 = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Initialize a varible
count_of_four = 0

# Iterate through each element in the tuple
for num in tuple1:
    # Increment the counter if the current element is 4(value=2)
    if num == 4:
        count_of_four += 1

# Print the count of occurrences
print("Result:", count_of_four)  # Output: 3


# Q2: Convert a list to a tuple

# Create a sample list
list1 = [5, 10, 7, 4, 15, 3]

# Convert the list to a tuple using the tuple() constructor
tuple1 = tuple(list1)

# Print the resulting tuple
print("Result:", tuple1)  # Output: (5, 10, 7, 4, 15, 3)


# Q3: Calculate the sum of the numbers in a given tuple

# Create a sample list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Initialize a variable to store the sum
total_sum = 0

# Iterate through each tuple in the list
for tup in tuples_list:
    # Iterate through each number in the tuple
    for num in tup:
        # Add the current number to the total sum
        total_sum += num

# Print the calculated sum
print("Sum of values in the tuples:", total_sum)  # Output: 21


# Q4: Iterate the given tuples and print employee records

# Create sample tuples for employees
employee1 = ("Aman", 101, "Human Resources", 60000)
employee2 = ("Samirul", 102, "Marketing", 55000)
employee3 = ("Harry", 103, "Engineering", 75000)

# Create a list to store the employee tuples
employee_list = [employee1, employee2, employee3]

# Print a header
print("Employee Records:")

# Iterate through each employee tuple
for employee in employee_list:
    # Extract information from the tuple
    name, employee_id, department, salary = employee

    # Print the employee information
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Salary: ₹",salary)
    print()