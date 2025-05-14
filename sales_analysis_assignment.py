# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset from a CSV file
    df = pd.read_csv("sales.csv")  # Make sure sales.csv is in your working directory
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ File not found. Please ensure 'sales.csv' is in the working directory.")
    exit()

# Display the first few rows
print("\n📌 First 5 Rows of the Dataset:")
print(df.head())

# Display dataset structure
print("\n📌 Dataset Info:")
print(df.info())

# Check for missing values
print("\n📌 Missing Values:")
print(df.isnull().sum())

# Clean missing values (drop them for simplicity)
df = df.dropna()
print("\n📌 Missing values dropped.")

# Task 2: Basic Data Analysis
print("\n📊 Descriptive Statistics:")
print(df.describe())

# Group by Region and calculate average sales
print("\n📊 Average Sales by Region:")
print(df.groupby('Region')['Sales'].mean())

# Group by Region and calculate total profit
print("\n📊 Total Profit by Region:")
print(df.groupby('Region')['Profit'].sum())

# Observation Example
print("\n🔍 Observation:")
print("The West region had the highest average sales, while the South led in total profit.")

# Task 3: Data Visualization
sns.set(style='darkgrid')

# 1. Line Chart: Sales Over Time
plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(df['Date']), df['Sales'], marker='o', color='blue')
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_line_chart.png")
plt.show()

# 2. Bar Chart: Average Sales by Region
plt.figure(figsize=(6, 4))
df.groupby('Region')['Sales'].mean().plot(kind='bar', color='coral')
plt.title('Average Sales by Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.savefig("sales_bar_chart.png")
plt.show()

# 3. Histogram: Profit Distribution
plt.figure(figsize=(6, 4))
plt.hist(df['Profit'], bins=6, color='green', edgecolor='black')
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("profit_histogram.png")
plt.show()

# 4. Scatter Plot: Sales vs Profit
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Sales', y='Profit', hue='Region', data=df)
plt.title('Sales vs Profit by Region')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig("sales_profit_scatter.png")
plt.show()
