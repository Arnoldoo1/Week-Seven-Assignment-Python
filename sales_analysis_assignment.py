# Week 6 Assignment: Analyzing Sales Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate loading a CSV file (replace this with pd.read_csv('sales.csv') if needed)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Region': ['North', 'South', 'East', 'West'] * 3,
    'Sales': [2000, 2500, 1800, 2200, 2100, 2600, 1900, 2300, 2150, 2700, 2000, 2400],
    'Profit': [300, 400, 250, 350, 310, 410, 260, 360, 315, 420, 280, 390]
}
df = pd.DataFrame(data)

# Task 1: Explore the dataset
print("📌 First 5 Rows of the Dataset:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Missing Values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\n📊 Descriptive Statistics:")
print(df.describe())

print("\n📊 Average Sales by Region:")
print(df.groupby('Region')['Sales'].mean())

print("\n📊 Total Profit by Region:")
print(df.groupby('Region')['Profit'].sum())

# Task 3: Visualizations
sns.set(style='darkgrid')

# 1. Line chart: Sales over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig("sales_line_chart.png")
plt.show()

# 2. Bar chart: Average sales by region
plt.figure(figsize=(6, 4))
df.groupby('Region')['Sales'].mean().plot(kind='bar', color='coral')
plt.title('Average Sales by Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.savefig("sales_bar_chart.png")
plt.show()

# 3. Histogram: Distribution of Profit
plt.figure(figsize=(6, 4))
plt.hist(df['Profit'], bins=6, color='green', edgecolor='black')
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("profit_histogram.png")
plt.show()

# 4. Scatter plot: Sales vs Profit
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Sales', y='Profit', hue='Region', data=df)
plt.title('Sales vs Profit by Region')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig("sales_profit_scatter.png")
plt.show()
