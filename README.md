☕ Cafe Sales Data Cleaning & Analysis Project

📌 Project Overview

This project focuses on cleaning and analyzing a dirty cafe sales dataset.
The dataset contains several real-world data quality issues such as:

- Missing values
- Invalid entries (e.g., "ERROR", "UNKNOWN")
- Incorrect data types
- Inconsistent calculations
- Duplicate records

The main objective of this project is to clean the dataset and prepare it for analysis using Python and Pandas, followed by generating meaningful insights using Matplotlib visualizations.

This project demonstrates the data cleaning workflow used by data analysts and data engineers in real-world scenarios.

---

📂 Dataset Description

The dataset represents cafe sales transactions and includes the following columns:

Column| Description
Transaction ID| Unique ID for each transaction
Item| Name of the item purchased
Quantity| Number of items purchased
Price Per Unit| Price of one item
Total Spent| Total amount spent in the transaction
Payment Method| Payment type used by the customer
Location| Order location (In-store / Takeaway)
Transaction Date| Date of the transaction

---

🧹 Data Cleaning Process

The dataset contains several data quality issues that need to be handled before analysis.

1️⃣ Handling Invalid Values

Some columns contain invalid entries such as:

- "ERROR"
- "UNKNOWN"

These values are replaced with NaN to treat them as missing values.

Reason:
Invalid entries cannot be used for analysis and must be standardized.

---

2️⃣ Handling Missing Values

Several columns contain missing values.

Different strategies are used depending on the column type:

Column| Strategy
Item| Replace with ""Unknown Item""
Quantity| Fill using median value
Price Per Unit| Fill using median value
Payment Method| Replace with ""Unknown""
Location| Replace with ""Unknown""

Reason:
Handling missing values ensures that the dataset remains usable without losing too much data.

---

3️⃣ Fixing Data Types

Some columns may have incorrect data types.

The following conversions are applied:

Column| Correct Data Type
Quantity| Integer
Price Per Unit| Float
Total Spent| Float
Transaction Date| Datetime

Reason:
Correct data types are required for proper analysis and visualization.

---

4️⃣ Data Consistency Check

A validation check is performed to ensure:

Total Spent = Quantity × Price Per Unit

If inconsistencies are found, the Total Spent value is recalculated.

Reason:
This ensures data accuracy and consistency.

---

5️⃣ Duplicate Records Removal

Duplicate transactions are identified using Transaction ID and removed.

Reason:
Duplicate data can distort analysis results.

---

6️⃣ Date Cleaning

The "Transaction Date" column is cleaned and converted to datetime format.

Additional time-based features are created:

- Month
- Day
- Weekday

Reason:
These features allow time-based sales analysis.

---

7️⃣ Outlier Detection

Extreme values in columns like Quantity or Price Per Unit are checked to detect possible data entry errors.

Reason:
Outliers can distort statistical analysis and visualizations.

---

📊 Exploratory Data Analysis (EDA)

After cleaning the dataset, several insights are explored using Matplotlib.

1️⃣ Most Popular Items

A bar chart is used to identify the most frequently sold items.

Insight:
Helps understand customer preferences.

---

2️⃣ Revenue by Item

A bar chart shows which items generate the highest revenue.

Insight:
Identifies the most profitable products.

---

3️⃣ Payment Method Distribution

A pie chart is used to visualize the distribution of payment methods.

Insight:
Shows how customers prefer to pay.

---

4️⃣ Sales by Location

A bar chart compares In-store vs Takeaway sales.

Insight:
Helps understand customer ordering behavior.

---

5️⃣ Sales Trend Over Time

A line chart is used to analyze sales trends over time.

Insight:
Helps identify peak sales periods.

---

6️⃣ Price vs Quantity Relationship

A scatter plot is used to explore the relationship between item price and quantity sold.

Insight:
Shows how pricing affects purchasing behavior.

---

🛠 Tools & Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook / Google Colab
- GitHub

---

🎯 Key Skills Demonstrated

This project demonstrates several essential Data Analyst skills:

- Data Cleaning
- Data Quality Assessment
- Handling Missing Data
- Data Validation
- Exploratory Data Analysis (EDA)
- Data Visualization
- Python Data Analysis Workflow

---

📈 Conclusion

Cleaning raw data is a crucial step in any data analysis workflow.
This project demonstrates how a messy real-world dataset can be transformed into a clean and reliable dataset suitable for analysis.

After cleaning the dataset, meaningful insights can be extracted to understand sales patterns, customer preferences, and revenue trends.

---

👨‍💻 Author

Sanju Devrari

Aspiring Data Analyst | Python | SQL | Data Cleaning | Data Visualization
