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
'''
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
''' 


# I have a dataset of daily temperatures over a week, and I want to calculate statistics like the mean, median, variance and standard deviation of temperatures. Can you please generate a complete program using Python numpy.


import numpy as np

# Input dataset: daily temperatures over a week (in degrees Celsius)
temperatures = np.array([23.4, 25.1, 22.8, 24.5, 26.0, 21.9, 23.7])

# Calculate statistics
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
variance_temp = np.var(temperatures)
std_deviation_temp = np.std(temperatures)

# Print the results
print("Daily Temperatures (°C):", temperatures)
print(f"Mean Temperature: {mean_temp:.2f}°C")
print(f"Median Temperature: {median_temp:.2f}°C")
print(f"Temperature Variance: {variance_temp:.2f}")
print(f"Standard Deviation of Temperature: {std_deviation_temp:.2f}")
