import pandas as pd

# Load the dataset (assuming the file is 'beer_data.csv')
df = pd.read_csv("beer_data.csv")

# Rename column if necessary (make sure column names match)
df.rename(columns={'Alcohol(pct)': 'Alcohol'}, inplace=True)

# Compute Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Alcohol'].quantile(0.25)
Q3 = df['Alcohol'].quantile(0.75)

# Compute Interquartile Range (IQR)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
filtered_df = df[(df['Alcohol'] >= lower_bound) & (df['Alcohol'] <= upper_bound)]

# Compute mean and median without outliers
mean_without_outliers = round(filtered_df['Alcohol'].mean(), 2)
median_without_outliers = round(filtered_df['Alcohol'].median(), 2)

# Print results
print("Mean without outliers:", mean_without_outliers)
print("Median without outliers:", median_without_outliers)
