# Q1: Calculate the mean of a dictionary

# Create a sample dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the sum of values
total_sum = sum(test_dict.values())

# Calculate the number of values
num_values = len(test_dict)

# Calculate the mean
mean = total_sum / num_values

# Print the mean
print("Mean:", mean)  # Output: 6.2


# Q2: WAP to Concatenate dictionaries

# Create sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

# Create an empty dictionary to store the concatenated result
result_dict = {}

# Combine dictionaries using dictionary unpacking
result_dict.update(dic1)
result_dict.update(dic2)

# Print the concatenated dictionary
print("Expected Result:", result_dict)  # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Q3: Get key, value, and item in a dictionary

# Create a sample dictionary
dict_num = {1: 10, 2: 20, 3: 30}

# Print the header
print("key   value")

# Iterate through the dictionary items
for key, value in dict_num.items():
    # Print the key and value
    print(f"{key}      {value}") 
# output is key   value    
           # 1      10
           # 2      20
           # 3      30


# Q 4: Get key, value, and item in a dictionary, dropping items with None values

# Create a dictionary with None values
input_dict = {1: 10, 2: 20, 3: None, 5: None}

# Create a new dictionary to store items without None values
new_dict = {}

# Iterate through the dictionary items
for key, value in input_dict.items():
    # Add the key-value pair to the new dictionary if the value is not None
    if value is not None:
        new_dict[key] = value

# Print the new dictionary
print("Dictionary with Empty Items Dropped:")
print(new_dict)  # Output: {1: 10, 2: 20}
