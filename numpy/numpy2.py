# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# print(np.pi)

# weather data analysis
"""
import numpy as np

# Daily temperatures (°C) recorded over a week
temperatures = np.array([23, 25, 20, 22, 26, 24, 21])

# Calculate statistics

average_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("Average Temperature:", average_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
""" 

# Ecommerce analysis
""" 
import numpy as np

# Price and quantity of products sold
prices = np.array([10, 20, 15, 30])
quantities = np.array([100, 50, 80, 30])

# Calculate total revenue for each product
revenue = prices * quantities

print("Revenue for each product:", revenue)
print("Total Revenue:", np.sum(revenue))
"""

# .Hi! Can you please generate a program to identify overweight individuals using numpy.
import numpy as np

# Example data
names = ["Alice", "Bob", "Charlie", "Diana"]
weights = [68, 85, 54, 95]  # in kilograms
heights = [1.65, 1.75, 1.60, 1.80]  # in meters

# Convert lists to NumPy arrays
weights = np.array(weights)
heights = np.array(heights)

# Calculate BMI (BMI = weight / height^2)
bmi = weights / (heights ** 2)

# Identify indices where BMI > 25
overweight_indices = np.where(bmi > 25)

# Extract names of overweight individuals
overweight_individuals = np.array(names)[overweight_indices]

# Display results
print("Overweight individuals:", overweight_individuals.tolist())