import FreeSimpleGUI as sg
import csv

def guardar_gasto(Monto, Categoria, Fecha):
    with open("datos.csv", "a", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([f"El monto es de: {Monto}"])
        writer.writerow([f"La categoría es: {Categoria}"])
        writer.writerow([f"La fecha es: {Fecha}"])


def ver_resumen():

    with open("datos.csv", "r") as archivo:
        contenido = archivo.read()
    return contenido
