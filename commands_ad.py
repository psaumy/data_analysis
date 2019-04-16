import csv
from your_own_appname.models import ADR
ADR.objects.all()

with open('adrfile.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        p = ADR()
        p.load = row['load']
        p.cyl1 = float(row['cyl1'])
        p.cyl2 = float(row['cyl2'])
        p.cyl3 = float(row['cyl3'])
        p.mean = float(row['mean'])
        p.cov  = float(row['cov'][:-1])
        p.rsr  = float(row['rsr'])
        p.unknwn = (row['unknown'][:-1])
        p.save()
