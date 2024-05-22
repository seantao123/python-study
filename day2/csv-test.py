import csv
import pandas as pd
import matplotlib.pyplot as plt

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


titanic_data = pd.read_csv('titanic.csv')
titanic_data = titanic_data.dropna(subset=['Age'])
age_death_rate = titanic_data.groupby(pd.cut(titanic_data['Age'], bins=range(0, 90, 5)))['Survived'].mean()

age_death_rate.plot(kind='line', marker='o', color='red')
plt.title('Death Rate by Age')
plt.xlabel('Age Range')
plt.ylabel('Death Rate')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
