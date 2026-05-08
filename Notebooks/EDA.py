# Import pandas library for data handling and analysis
import pandas as pd

# Import matplotlib library for data visualization
import matplotlib.pyplot as plt


# GitHub raw CSV file path
path = 'https://raw.githubusercontent.com/SanjayDevrari/Cafe-Sales-Data-Cleaning-and-Analysis-Project/refs/heads/main/Data/cleaned_cafe_sales.csv'

# Read the CSV file and store it in a DataFrame
df = pd.read_csv(path, encoding='utf-8')

# Print the complete dataset
print(df)


# ---------------- PRODUCT WISE TOTAL SALES ---------------- #

# Group data by Item column and calculate total quantity sold
product_sales = df.groupby('Item')['Quantity'].sum()

# Create a bar chart for total product sales
product_sales.plot(kind='bar')

# Set chart title
plt.title("Product Wise Total Sales")

# Set label for X-axis
plt.xlabel("Products")

# Set label for Y-axis
plt.ylabel("Total Quantity Sold")

# Rotate product names on X-axis for better readability
plt.xticks(rotation=45)


# ---------------- PRODUCT WISE TOTAL REVENUE ---------------- #

# Group data by Item column and calculate total revenue
product_revenue = df.groupby("Item")["Total Spent"].sum()

# Set chart title
plt.title("Product Wise Total Revenue")

# Set label for X-axis
plt.xlabel("Products")

# Set label for Y-axis
plt.ylabel("Total Revenue")

# Create a bar chart for product revenue
product_revenue.plot(kind='bar')

# Rotate product names on X-axis for better readability
plt.xticks(rotation=45)


# Display the chart
plt.show()
