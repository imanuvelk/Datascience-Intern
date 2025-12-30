# Sales Data Analysis
# Week 3 - Developers Arena Data Science Internship

import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Handle missing values (clean & future-safe)
df['Quantity'] = df['Quantity'].fillna(0)
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# Calculate metrics
total_sales = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
max_sales = df['Total_Sales'].max()

# Best-selling product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Display report
print("\n📊 SALES ANALYSIS REPORT")
print(f"Total Sales: ₹{total_sales}")
print(f"Average Sales: ₹{average_sales:.2f}")
print(f"Highest Sale Value: ₹{max_sales}")
print(f"Best Selling Product: {best_product}")
