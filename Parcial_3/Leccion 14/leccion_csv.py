import csv
with open('hobbies.csv', 'r') as csv_archivo:
    datos = list(csv.reader(csv_archivo))

nombre = input('Nombre: ')
for x in datos[1:]:
    if nombre.capitalize() == x[0]:
        print(x[1])