import FreeSimpleGUI
import csv


def pedir_datos():
    nombre = input("Nombre del gasto: ")
    precio = float(input("Precio por unidad: "))
    veces = int(input("Veces por semana: "))
    meses = int(input("Tiempo en meses: "))
    return nombre, precio, veces, meses

def calcular_total(precio, veces, meses):
    semanas = meses * 4
    return precio * veces * semanas

def guardar_en_csv(nombre, precio, veces, meses, total, archivo="datos.csv"):
    with open(archivo, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nombre, precio, veces, meses, total])