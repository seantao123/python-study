from datetime import datetime, timedelta
import math

number = 9232324
if number % 2 == 0:
    print('even')
else:
    print('odd')

float = 6324.34343457
round = round(float)
print(round)
floor = math.floor(float)
print(floor)
ceiling = math.ceil(float)
print(ceiling)


string = 'today is tuesday, tomorrow is wednesday'
today, tomorrow = string.split(', ')
print(f"{tomorrow + ' ' + today}")


# today = ??
current_date = datetime.now()
print("Current date:", current_date)

# the day before yeasterday is
days_delta = 2
past_date = current_date - timedelta(days=days_delta)
print("Past date:", past_date)

# the day after tomoorw is
future_date = current_date + timedelta(days=days_delta)
print("Future date:", future_date)


current_date = datetime(year=2039, month=1, day=1)
bday = datetime(year=2005, month=11, day=10)
age = current_date.year - bday.year - ((current_date.month, current_date.day) < (bday.month, bday.day))
print("age", age)

value = True
print(not value)