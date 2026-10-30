import csv
import mysql.connector as s

ob = s.connect(
    host='localhost',
    user='root',
    password='',
    database='finance'
)
cu = ob.cursor()

def pft():
    with open(r"C:\Users\Somesh\Downloads\personal finance.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for i in reader:
            d = i[0]
            cat = i[1]
            amt = float(i[2])

            cu.execute("SELECT amount FROM tracker WHERE category = %s", (cat,))
            result = cu.fetchone()

            if result:
                update_query = """
                    UPDATE tracker 
                    SET amount = amount + %s, last_date = %s 
                    WHERE category = %s
                """
                cu.execute(update_query, (amt, d, cat))
            else:
                insert_query = """
                    INSERT INTO tracker (category, amount, last_date) 
                    VALUES (%s, %s, %s)
                """
                cu.execute(insert_query, (cat, amt, d))

        ob.commit()
        print("Finance tracked successfully ✅")

pft()

q = input("Do u want to see report(y/n): ")
if q == 'y':
    cu.execute("SELECT * FROM tracker")
    r = cu.fetchall()
    for row in r:
        print(row)
else:
    print("OKK")

cu.close()
ob.close()y