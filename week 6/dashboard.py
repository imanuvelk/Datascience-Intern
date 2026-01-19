import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Theme
sns.set_theme(style="whitegrid")

# Load data
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# ------------------ PLOT 1: BOX PLOT ------------------
plt.figure()
sns.boxplot(x='Product', y='Price', data=df)
plt.title("Price Distribution by Product")
plt.tight_layout()
plt.show()

# ------------------ PLOT 2: VIOLIN PLOT ------------------
plt.figure()
sns.violinplot(x='Product', y='Total_Sales', data=df)
plt.title("Sales Distribution by Product")
plt.tight_layout()
plt.show()

# ------------------ PLOT 3: HEATMAP ------------------
plt.figure()
corr = df[['Quantity', 'Price', 'Total_Sales']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ------------------ PLOT 4: 2×2 DASHBOARD ------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.barplot(ax=axes[0, 0], x='Product', y='Total_Sales', data=df)
axes[0, 0].set_title("Sales by Product")

sns.lineplot(ax=axes[0, 1], x='Month', y='Total_Sales', data=df)
axes[0, 1].set_title("Monthly Sales Trend")

sns.boxplot(ax=axes[1, 0], x='Region', y='Total_Sales', data=df)
axes[1, 0].set_title("Sales by Region")

sns.countplot(ax=axes[1, 1], x='Product', data=df)
axes[1, 1].set_title("Product Order Count")

plt.tight_layout()
plt.show()

# ------------------ PLOT 5: INTERACTIVE PLOTLY ------------------
fig = px.bar(
    df,
    x='Product',
    y='Total_Sales',
    color='Region',
    title="Interactive Product Sales by Region",
    hover_data=['Quantity', 'Price']
)

fig.show()
