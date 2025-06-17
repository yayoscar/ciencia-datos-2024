import csv

def comparador(productos):
    with open("comparador_de_precios.csv", mode="a", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow([productos])

d

