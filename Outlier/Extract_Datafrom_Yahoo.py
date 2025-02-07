import yfinance as yf
import pandas as pd

# Define stock symbol and time range
stock_symbol = "IBM"
start_date = "2018-01-01"
end_date = "2018-12-31"

# Download stock data from Yahoo Finance
ibm_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Reset index to make Date a column
ibm_data.reset_index(inplace=True)

# Format Date column to match the required format (e.g., "Dec 28, 2018")
ibm_data['Date'] = ibm_data['Date'].dt.strftime('%b %d, %Y')

# Rename columns only if the expected number of columns exist
expected_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

if len(ibm_data.columns) == len(expected_cols):
    ibm_data.columns = expected_cols  # Apply renaming only if the number of columns matches

# Ensure Volume is first converted to integer (to avoid float issue)
ibm_data['Volume'] = ibm_data['Volume'].fillna(0).astype(int)

# Apply comma formatting to Volume column
ibm_data['Volume'] = ibm_data['Volume'].map(lambda x: "{:,}".format(x))

# Remove extra row if present
if isinstance(ibm_data.iloc[0, 0], str) and "IBM" in ibm_data.iloc[0, 0]:
    ibm_data = ibm_data.iloc[1:].reset_index(drop=True)

# Save formatted data to a CSV file (without unwanted index or extra headers)
csv_file_path = "IBM_stock_data_cleaned.csv"
ibm_data.to_csv(csv_file_path, index=False)

# Print confirmation message
print(f"✅ Cleaned IBM stock data successfully saved to: {csv_file_path}")
