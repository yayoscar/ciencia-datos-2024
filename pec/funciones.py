import csv
from collections import defaultdict

def guardar_gasto(nombre_archivo, monto, categoria, fecha=""):
    with open(nombre_archivo, mode='a', newline='') as archivo:
        escrito = csv.writer(archivo)
        escrito.writerow([monto, categoria, fecha])

def obtener_resumen(nombre_archivo):
    resumen = defaultdict(float)
    total = 0.0

    try:
        with open(nombre_archivo, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                try:
                    monto = float(fila[0])
                    categoria = fila[1]
                    resumen[categoria] += monto
                    total += monto
                except (IndexError, ValueError):
                    continue
    except FileNotFoundError:
        pass  # Si el archivo no existe aún, simplemente devuelve vacío

    return resumen, total