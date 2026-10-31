# Business Sales Intelligence System

A Python-based project that analyses business sales data and converts raw CSV records into useful business insights.

The goal of this project is to understand sales performance, identify trends, and generate a simple business summary using Python.

## Features

- **Total Revenue:** Calculates overall revenue from sales records.
- **Highest-Selling Product:** Identifies the product with the highest number of units sold.
- **Category-wise Revenue:** Calculates revenue for each product category.
- **Best-Performing Month:** Finds the month with the highest total revenue.
- **Average Order Value (AOV):** Calculates average revenue per unique order.
- **Declining Sales Detection:** Identifies products whose revenue has decreased compared with the previous available month.
- **Business Summary:** Generates a text file containing the analysis results.

## Technologies Used

- Python
- CSV Module
- Dictionaries
- Functions
- Lambda and Map
- Data Aggregation
- Date Handling

## Dataset Structure

The project uses a CSV dataset with the following columns:

| Column | Description |
|---|---|
| OrderID | Unique order identifier |
| Product | Product name |
| Cat | Product category |
| SP | Selling price |
| Sales | Total units sold |
| Quantity | Quantity field |
| Date | Date of sale |

## How It Works

1. Reads sales records from a CSV file.
2. Processes and converts numerical values.
3. Groups sales data by product, category, and month.
4. Calculates business performance metrics.
5. Identifies declining sales trends.
6. Generates a business summary in a text file.

## Project Structure

```text
Business-Sales-Intelligence/
│
├── business_sales_data.csv
├── main.py
├── Business_Summary.txt
└── README.md
```

## How to Run

1. Clone or download this repository.
2. Make sure Python is installed.
3. Keep the CSV dataset in the project folder.
4. Run the Python program:

```bash
python main.py
```

5. Enter the CSV file path when prompted.

## Learning Objectives

This project focuses on practical Python programming and business data analysis, particularly:

- Working with structured CSV data.
- Using dictionaries for data aggregation.
- Applying functions to organise code.
- Comparing and analysing monthly sales.
- Extracting meaningful insights from business records.

---

**Project Type:** Python | Business Data Analysis

**Status:** Learning Project
