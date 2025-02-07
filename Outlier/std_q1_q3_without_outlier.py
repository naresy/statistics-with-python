import numpy as np
import pandas as pd

# Load the dataset
file_path = "../../beer.csv"
df = pd.read_csv(file_path)

# Extract the alcohol percentage column
alcohol_pct = df["Alcohol(pct)"]

# Calculate Q1 and Q3
Q1 = np.percentile(alcohol_pct, 25)
Q3 = np.percentile(alcohol_pct, 75)

# Calculate interquartile range (IQR)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
filtered_alcohol_pct = alcohol_pct[(alcohol_pct >= lower_bound) & (alcohol_pct <= upper_bound)]

# Recalculate Q1 and Q3 after removing outliers
Q1_corrected = np.percentile(filtered_alcohol_pct, 25)
Q3_corrected = np.percentile(filtered_alcohol_pct, 75)

# Calculate standard deviation without outliers
std_without_outliers = np.std(filtered_alcohol_pct, ddof=1)

# Print results rounded to three decimal places
print("Standard Deviation without outliers:", round(std_without_outliers, 3))
print("Q1 without outliers:", round(Q1_corrected, 3))
print("Q3 without outliers:", round(Q3_corrected, 3))
