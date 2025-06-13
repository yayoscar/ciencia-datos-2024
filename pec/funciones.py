import FreeSimpleGUI as sg
import csv
datos = [1,2,3]

def guardar_en_csv(fila):
    with open("datos.csv", "a", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(fila)

def leer_csv(fila):
    with open("datos.csv", "r") as archivo:
        leer = csv.reader(archivo)
    for fila in leer:
        datos.append()