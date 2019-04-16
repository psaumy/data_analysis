import csv
from titanic.models import Passenger
Passenger.objects.all()

with open('titanic.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        p = Passenger()
        p.name = row['name']
        p.gender = row['gender']
        p.survived = True if row['survived'] == '1' else False
        p.ticket_class = int(row['ticket_class'])
        p.embarked = row['embarked']
        p.age = float(row['age']) if row['age'] != '' else None
        p.save()
