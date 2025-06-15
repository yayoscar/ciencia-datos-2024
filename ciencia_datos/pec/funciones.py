import csv

def registro(aporte):
    with open('registro_de_aportes.csv','a',newline='') as archivo:
        ahorro = csv.writer(archivo)
        ahorro.writerow([aporte])
