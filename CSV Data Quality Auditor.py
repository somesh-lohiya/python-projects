import csv

def auditor(file):
    with open(file, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        records = list(reader)

    return records


def duplicates(records):
    ids = {}
    dup = []

    for record in records:
        cid = record["Customer_ID"]

        if cid in ids:
            ids[cid] += 1
        else:
            ids[cid] = 1

    for cid in ids:
        if ids[cid] > 1:
            dup.append((cid, ids[cid]))

    print("Duplicate IDs:", dup)


def missing(record):
    miss = []

    for key, value in record.items():
        if value is None or value.strip() == "":
            miss.append(key)

    if miss:
        return record["Customer_ID"], miss

    return None


file = input("Input CSV file location: ")

records = auditor(file)

x = int(input('''What do you want to do?
1. Check Duplicate
2. Check Missing Value
3. Both
Enter choice: '''))

if x == 1:
    duplicates(records)

elif x == 2:
    for record in records:
        result = missing(record)

        if result:
            print(result)

elif x == 3:
    duplicates(records)

    for record in records:
        result = missing(record)

        if result:
            print(result)

else:
    print("Invalid choice!")