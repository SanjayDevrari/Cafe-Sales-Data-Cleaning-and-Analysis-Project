# ---------------------------------------------------------
# Cafe Sales Data - Basic Data Inspection
# ---------------------------------------------------------
# This section loads the dataset and performs initial
# inspection to understand the structure and contents
# of the data before cleaning.
# ---------------------------------------------------------

# Import the pandas library for data manipulation
import pandas as pd
# Import numpy (needed to use NaN values)
import numpy as np
# Define the dataset path (CSV file hosted on GitHub)
path = "https://raw.githubusercontent.com/SanjayDevrari/Cafe-Sales-Data-Cleaning-and-Analysis-Project/refs/heads/main/Data/dirty_cafe_sales.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(path, encoding="utf-8")

# ---------------------------------------------------------
# 1️⃣ Check the shape of the dataset
# ---------------------------------------------------------
print("Dataset Shape (Rows, Columns):")
print(df.shape)


# ---------------------------------------------------------
# 2️⃣ Display the first few rows
# ---------------------------------------------------------
print("\nFirst 5 Rows of Dataset:")
print(df.head())


# ---------------------------------------------------------
# 3️⃣ Display dataset information
# ---------------------------------------------------------
print("\nDataset Information:")
print(df.info())

# ---------------------------------------------------------
# 4️⃣ Statistical summary of numerical columns
# ---------------------------------------------------------
print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------------------------------
# 1️⃣ Check Missing Values
# ---------------------------------------------------------
print("Missing Values in Each Column:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 2️⃣ Replace Invalid Entries with NaN
# ---------------------------------------------------------
df.replace(["ERROR", "UNKNOWN"], np.nan, inplace=True)


# ---------------------------------------------------------
# 3️⃣ Check Duplicate Records
# ---------------------------------------------------------
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# ---------------------------------------------------------
# 4️⃣ Remove Duplicate Records
# ---------------------------------------------------------
df.drop_duplicates(inplace=True)
