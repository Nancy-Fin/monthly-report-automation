import csv

monthly_totals = {}

with open("transactions.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row["date"][:7]
        amount = float(row["amount"])
        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

print("Monthly spending report")
print("-----------------------")
for month, total in monthly_totals.items():
    print(f"{month}: {total:.2f}")