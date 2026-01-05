# E-commerce Sales Analysis with Visualization
# Week 4 - Developers Arena Data Science Internship

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
df['Quantity'] = df['Quantity'].fillna(0)
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# ------------------ ANALYSIS ------------------

# Sales by product
sales_by_product = df.groupby('Product')['Total_Sales'].sum()

# Monthly sales trend
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# ------------------ VISUALIZATION ------------------

# Bar Chart: Sales by Product
plt.figure()
sales_by_product.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# Line Chart: Monthly Sales Trend
plt.figure()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("visualizations/sales_trend.png")
plt.close()

# ------------------ REPORT OUTPUT ------------------

print("📊 E-COMMERCE SALES ANALYSIS REPORT")
print(f"Total Revenue: ₹{df['Total_Sales'].sum():,.2f}")
print(f"Best Selling Product: {sales_by_product.idxmax()}")
print("Visualizations saved in 'visualizations/' folder")
