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

# Count the number of transactions for each payment method
payment_count = df['Payment Method'].value_counts()

# Create a pie chart for payment methods
plt.pie(
    payment_count,                    # Data values
    labels=payment_count.index,      # Labels for each section
    autopct='%1.1f%%'                # Show percentage with 1 decimal place
)

# Save the pie chart as a PNG image with high quality
plt.savefig("payment_method_pie_chart.png", dpi=300)

# Download the saved pie chart file in Google Colab
files.download("payment_method_pie_chart.png")

# Display the pie chart
plt.show()


# ---------------- SALES BY LOCATION ---------------- #

# Count total sales for each location
sales_area = df['Location'].value_counts()

# Print sales count by location
print(sales_area)

# Create a bar chart for sales by location
plt.bar(sales_area.index, sales_area.values)

# Set chart title
plt.title("Sales by Location")

# Set label for X-axis
plt.xlabel("Location")

# Set label for Y-axis
plt.ylabel("Sales")

# Save the bar chart as a PNG image
plt.savefig("sales_by_location_bar_chart.png", dpi=300)

# Download the saved bar chart file in Google Colab
files.download("sales_by_location_bar_chart.png")

# Display the bar chart
plt.show()
