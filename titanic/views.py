import json

from django.db.models import Count, Q
from django.shortcuts import render
from titanic.models import Passenger
from django.conf import settings

def home(request):
    return render(request, 'home.html', {})

def readTable(request):
    csvFile = settings.BASE_DIR + "/adr.csv"

    tableData = []
    tableHeaders = []

    with open(csvFile) as csvData:
        reader = csvData.readlines()
        i = 0
        for row in reader:
            if i == 0:
                tableHeaders = row.split(",")
                i = i + 1
            else:
                tableData.append(row.split(","))
    print(tableHeaders)
    print(tableData)

    return render(request, 'afim.html', {'tableHeaders': tableHeaders, 'tableData': tableData}) 

def bargraph(request):
    import csv 
    csvFile = settings.BASE_DIR + "/adr.csv"

    categories = []
    cyl1_data = []
    cyl2_data = []
    cyl3_data = []

    with open(csvFile) as csvData:

        reader = csv.DictReader(csvData)
        print(reader)

        for row in reader:
            print(row)
            categories.append(row['load'])
            cyl1_data.append(float(row['cyl1']))
            cyl2_data.append(float(row['cyl2']))
            cyl3_data.append(float(row['cyl3']))

    cyl1_series = {
        'name': 'Cyl1',
        'data': cyl1_data,
        'color': 'red'
    }

    cyl2_series = {
        'name': 'Cyl2',
        'data': cyl2_data,
        'color': 'green'
    }

    cyl3_series = {
        'name': 'Cyl3',
        'data': cyl3_data,
        'color': 'blue'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'AFIM Deviation Ratio[ADR]'},
        'xAxis': {'categories': categories},
        'series': [cyl1_series, cyl2_series, cyl3_series]
    }

    return render(request, 'afim_g.html', {'chart': chart}) 



def adr_view(request):
    import csv

    with open('/Users/rajatsingh/pwork/saumya/data_analysis/adr.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = {}
        for row in reader:
            for header, value in row.items():
              if header in data:
                try:
                    data[header].append(float(value))
                except ValueError:
                    data[header].append(value)
              else:
                try:
                    data[header] = [float(value)]
                except ValueError:
                    data[header] = [value]
    
    with open('/Users/rajatsingh/pwork/saumya/data_analysis/adr.csv', 'r') as f:
        reader = csv.reader(f)
        field = []
        for row in reader:
            field.append(row)


    print(field)
    return render(request, 'ticket_class_2.html', {
        'categories': data['load'],
        'cyl1': data['cyl1'],
        'cyl2': (data['cyl2']),
        'cyl3': (data['cyl3']),
        'field': (field)

    })

def ticket_class_view(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'ticket_class.html', {'dataset': dataset})

def ticket_class_view_2(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    categories = list()
    survived_series = list()
    not_survived_series = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    return render(request, 'ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series)
    })

def embarked_view(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .annotate(survived_count=Count('embarked', filter=Q(survived=True)),
                  not_survived_count=Count('embarked', filter=Q(survived=False))) \
        .order_by('embarked')

    embarked = list()
    survived_series = list()
    not_survived_series = list()

    for entry in dataset:
        embarked.append('%s Port' % entry['embarked'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    context = {
        'embarked': json.dumps(embarked),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series)
    }
    return render(request, 'embarked.html', context)