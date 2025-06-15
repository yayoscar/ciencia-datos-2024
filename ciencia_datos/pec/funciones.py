import csv

def registro(aporte):
    with open("registro_de _aportes.csv", mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([aporte])



