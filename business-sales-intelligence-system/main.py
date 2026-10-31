import csv

def intelligence():
    with open(file, 'r', newline="") as f:
        reader = csv.reader(f)
        next(reader)
        readers = list(reader)
    return readers


def total_revenue(readers):
    trevenue = 0
    for i in readers:
        trevenue += int(i[3]) * int(i[4])
    return trevenue


def high(readers):
    c = 0
    n = ''
    for i in readers:
        if c < int(i[4]):
            c = int(i[4])
            n = i[1]
    return c, n


def rbc(readers):
    rebc = {}
    for i in readers:
        if i[2] in rebc:
            rebc[i[2]] += int(i[3]) * int(i[4])
        else:
            rebc[i[2]] = int(i[3]) * int(i[4])
    return rebc


def bfm(readers):
    trr = {}
    for i in readers:
        month = i[6][:7]
        t = int(i[3]) * int(i[4])

        if month in trr:
            trr[month] += t
        else:
            trr[month] = t

    n = max(trr, key=trr.get)
    return n, trr[n]


def vpo(readers):
    tr = total_revenue(readers)
    to = len(set(i[0] for i in readers))
    if to == 0:
        return 0
    return tr / to


def declining(readers):
    sales = {}

    for i in readers:
        product = i[1]
        month = i[6][:7]
        revenue = int(i[3]) * int(i[4])

        if product not in sales:
            sales[product] = {}

        if month in sales[product]:
            sales[product][month] += revenue
        else:
            sales[product][month] = revenue

    dec = []

    for product in sales:
        months = sorted(sales[product])
        if len(months) >= 2:
            if sales[product][months[-1]] < sales[product][months[-2]]:
                dec.append(product)

    return dec


def summary(readers):
    with open("Business_Summary.txt", "w") as f:
        f.write(f"Total Revenue: {total_revenue(readers)}\n")
        f.write(f"Highest Selling Product: {high(readers)}\n")
        f.write(f"Revenue By Category: {rbc(readers)}\n")
        f.write(f"Best Performing Month: {bfm(readers)}\n")
        f.write(f"Average Order Value: {vpo(readers)}\n")
        f.write(f"Products With Declining Sales: {declining(readers)}\n")


file = input("Enter CSV file path: ")
readers = intelligence()

print("Total Revenue:", total_revenue(readers))
print("Highest Selling Product:", high(readers))
print("Revenue By Category:", rbc(readers))
print("Best Performing Month:", bfm(readers))
print("Average Order Value:", vpo(readers))
print("Declining Products:", declining(readers))

summary(readers)
