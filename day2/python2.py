# first name, last name, gender, height, bday, phone
from datetime import datetime, date

seantao = {
    'first name': 'sean',
    'last name': 'tao',
    'male': True,
    'height': 193,
    'bday': datetime(2005, 11, 10),
    'phone': '(408)228-7969'
}

# Create Read Update Delete
seantao['address'] = '1587 four oaks cir., CA'
print(seantao)

print(seantao['male'])

seantao['male'] = False
print(seantao)

del seantao['address']
print(seantao)

rohit = {
    'first name': 'Rohit',
    'last name': 'pavurari',
    'male': True,
    'height': 175,
    'bday': datetime(2005, 11, 10),
    'phone': '(408)000-7969'
}


# array 
students = [seantao, rohit]
print(students)

# CRUD
jordan = {
    'first name': 'jordan',
    'last name': 'delos reyes',
    'male': True,
    'height': 180,
    'bday': datetime(2005, 4, 20),
    'phone': '(408)000-0000'
}

# students.append(jordan)
students.insert(1, jordan)
print(students)

print(students[2])


harsh = {
    'first name': 'harsh',
    'last name': 'panchal',
    'male': True,
    'height': 180,
    'bday': datetime(2005, 6, 20),
    'phone': '(408)000-0001'
}
students[1]=harsh
print(students)

del students[1]
print(students)