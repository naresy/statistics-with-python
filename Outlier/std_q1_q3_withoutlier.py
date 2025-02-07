import numpy as np
import pandas as pd

df=pd.read_csv("../../beer.csv")
df.rename(columns={'Alcohol(pct)': 'Alcohol'}, inplace=True)
std=round(df['Alcohol'].std(),3)
Q1=round(df['Alcohol'].quantile(0.25),3)
Q3=round(df['Alcohol'].quantile(0.75),3)
print("Standard deviation with outliers:", std)
print("Q1 (First quartile) with outliers:", Q1)
print("Q3 (Third quartile) with outliers:", Q3)

