import pandas as pd

# Load the CSV file
file_path = "IBM_stock_data_cleaned.csv"  # Ensure this is the correct path
df = pd.read_csv(file_path)

# Check if the first row contains "IBM" and remove it
if df.iloc[0].astype(str).str.contains("IBM").any():
    df = df.iloc[1:].reset_index(drop=True)

# Save the cleaned data back to a new CSV file
cleaned_file_path = "IBM_stock_data_final_fixed.csv"  # Change path if necessary
df.to_csv(cleaned_file_path, index=False)

print(f"✅ Cleaned IBM stock data saved to: {cleaned_file_path}")
