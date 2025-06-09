import csv
import FreeSimpleGUI as sg

def prepara_datos(valor):
    monto = valor['monto']
    categoria = valor['categoria']
    fecha = valor['fecha']
    fila = [monto, categoria, fecha]
    return fila

def añade_csv(fila):
    with open("datos.csv", "a", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(fila)


def es_numerico(fila):
    valor = fila[0]
    try:
        valor= float(valor)
        if float(valor).is_integer():
            valor = int(valor)
        return True
    except ValueError:
        sg.popup("No se puede guardar, el valor de monto debe ser un número", title="Error")