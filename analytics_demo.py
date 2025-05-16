import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SalesData_Taruni.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Add a new column for profit margin
df['Profit_Margin'] = df['Profit'] / df['Sales']

# Show summary statistics
print("\nSummary Stats:")
print(df.describe())

# Create a scatter plot: Ad Spend vs Sales
sns.scatterplot(x='Ad_Spend', y='Sales', data=df)
plt.title("Ad Spend vs Sales")
plt.show()