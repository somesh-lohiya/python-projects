# Personal Finance Tracker (Python + MySQL)

A simple Python program that reads daily personal expenses from a CSV file and updates a MySQL database. It automatically adds up expenses under the same category so you can track total spending.

---

## 📌 What This Project Does

- Reads expense records (`Date`, `Category`, `Amount`) from a CSV file.
- Checks if the expense category already exists in the MySQL table:
  - If it exists: Adds the new amount to the existing total and updates the date.
  - If it is new: Inserts a new record for that category.
- Displays an aggregated spending report directly on the screen.

---

## 🛠️ Tech Used

- **Language:** Python
- **Database:** MySQL
- **Modules:** `csv`, `mysql-connector-python`

---

## 🗄️ Database Setup (MySQL)

Create the database and table before running the code:

```sql
CREATE DATABASE finance;
USE finance;

CREATE TABLE tracker (
    category VARCHAR(50) PRIMARY KEY,
    amount FLOAT,
    last_date VARCHAR(20)
);
