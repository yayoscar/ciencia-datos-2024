import csv

def guardar_en_csv(meta, semanas, aporte):
    with open("datos.csv", "a", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow([meta, semanas, aporte])

def leer_csv():
    try:
        with open("datos.csv", "r") as archivo:
            return list(csv.reader(archivo))
    except FileNotFoundError:
        return []