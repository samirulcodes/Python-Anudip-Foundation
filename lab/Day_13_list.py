# Q1: Sum all the items in a list

# Create a list
my_list = [1, 2, 3, 4, 5]

# Initialize a variable for storing sum
total_sum = 0

# Iterate through each item in the list
for num in my_list:
    total_sum += num

# Print the calculated sum
print("Sum of all items is :", total_sum)  # Output: 15


# Q2: Get the largest and smallest number from a list without builtin functions

# Create a sample list
my_list = [10, 5, 20, 3, 8]

# Assume the first element is both the largest and smallest
largest  = my_list[0]
smallest= my_list[0]

# Iterate through the list starting from the second element (index 1)
for num in my_list[1:]:
    # if the current number is greater
    if num > largest:
        largest = num

    # if the current number is smaller
    if num < smallest:
        smallest = num

# Print the results
print("Largest number:", largest)  # Output: 20
print("Smallest number:", smallest)  # Output: 3


# Q 3: Find duplicate values from a list and display those

# Create a list
my_list = [1, 2, 3, 1, 4, 2, 5]

# Create an empty set for storing unique elements
unique_elements = set()

# Create an empty set for storing duplicate elements
duplicate_elements = set()

# Iterate through each item in the list
for num in my_list:
    # If the item is already in the unique_elements set, it's a duplicate
    if num in unique_elements:
        duplicate_elements.add(num)
    else:
        unique_elements.add(num)

# Print the duplicate elements
print("Duplicate values:", duplicate_elements)  # Output: {1, 2}


# Q 4: Split a given list into two parts where the length of the first part is given

# Create a list
my_list = [1, 2, 3, 4, 5, 6, 7]

# Specify the desired length of the first part
length_of_first_part = 3

# Split the list using slicing
first_part = my_list[:length_of_first_part]
second_part = my_list[length_of_first_part:]

# Print the split lists
print("Splitted list:", (first_part, second_part))  # Output: ([1, 2, 3], [4, 5, 6, 7])


# Q5: Traverse a given list in reverse order, and print the elements with the original index

# Create a list
my_list = ['red', 'green', 'white', 'black']

# Get the length of the list
list_length = len(my_list)

# Iterate through the list in reverse order
for i in range(list_length - 1, -1, -1):
    # Print the element with its original index
    print(my_list[i])

# Output:
# black
# white
# green
# red