import csv

def calcular_ahorro(nombre, precio, veces_semana, meses):
    gasto_total = precio * veces_semana * 4 * meses
    return gasto_total

def guardar_datos(nombre, precio, veces, meses, ahorro, archivo="datos.csv"):
    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nombre, precio, veces, meses, ahorro])