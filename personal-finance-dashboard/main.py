import csv
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="finance"
)
cursor = con.cursor()


def track_finance(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            date = row[0]
            category = row[1]
            amount = float(row[2])

            cursor.execute("SELECT amount FROM tracker WHERE category = %s", (category,))
            record = cursor.fetchone()

            if record:
                update_query = """
                    UPDATE tracker 
                    SET amount = amount + %s, last_date = %s 
                    WHERE category = %s
                """
                cursor.execute(update_query, (amount, date, category))
            else:
                insert_query = """
                    INSERT INTO tracker (category, amount, last_date) 
                    VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (category, amount, date))

        con.commit()
        print("Finance tracked successfully!")


file_name = input("Enter CSV file name (e.g., expenses.csv): ")

track_finance(file_name)

choice = input("Do you want to see the report? (y/n): ")

if choice.lower() == "y":
    cursor.execute("SELECT * FROM tracker")
    rows = cursor.fetchall()

    print("\n--- Expense Summary ---")
    print("Category | Total Amount | Last Date")
    print("-" * 35)
    for r in rows:
        print(f"{r[0]} | Rs. {r[1]} | {r[2]}")

cursor.close()
con.close()
