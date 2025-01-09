# Q1: Get Only Unique Items from Two Sets
# Create two sets 
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70}  

# Merge all unique elements from both sets using the union() method
unique_items = set1.union(set2) 

# Print the result
print("Result:", unique_items)  
# Output: {70, 40, 10, 50, 20, 60, 30}


# Q2: Return a Set of Elements Present in Set A or B, but not Both

# Create two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# using the symmetric_difference() method, finding elements that are in either set1 or set2
symmetric_difference = set1.symmetric_difference(set2)
print("Result:", symmetric_difference) 
# Output: {20, 70, 10, 60}


# Q3: Check if Two Sets Have Any Elements in Common

# # Create two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# using the intersection() method to find the elements that are common to both set1 and set2
print("Result:\n", set1.intersection(set2))


# Q4: Remove Items from Set1 that are not Common to Both Set1 and Set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# using the intersection() method to find the elements that are common to both set1 and set2
common_elements = set1.intersection(set2)
print("Output:", common_elements)  # Output: {40, 50, 30}