import csv
with open('hobies.csv','r') as csv.archivo:
    datos=csv.reaer(csv.archivo)
nombre=input("nombre:  ")
for x in datos[1:]:
    if nombre ==x[0]:
        print(x[1])