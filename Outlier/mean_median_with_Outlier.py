import pandas as pd

# Load the dataset (Make sure to replace 'beer.csv' with your actual file path if needed)
df = pd.read_csv("../../beer.csv")

# Rename the alcohol column for easier reference
df.rename(columns={'Alcohol(pct)': 'Alcohol'}, inplace=True)

# Compute the mean and median WITH outliers, rounded to three decimal places
mean_with_outliers = round(df['Alcohol'].mean(), 3)
median_with_outliers = round(df['Alcohol'].median(), 3)

# Print the results
print("Mean with outliers:", round(mean_with_outliers,3))
print("Median with outliers:", round(median_with_outliers,3))
