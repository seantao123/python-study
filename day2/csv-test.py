import csv

csv_data = []
with open('titanic.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[5]:
            csv_data.append(row)

csv_age_data = []
for row in csv_data:
    if 20 < float(row[5]) < 30:
        csv_age_data.append(row)

size = len(csv_age_data)
print(size)

