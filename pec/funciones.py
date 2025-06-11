import csv
import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED


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

def leer_dict():
    with open('datos.csv', 'r') as csvfile:
        campos = ['monto', 'categoria', 'fecha']
        lector = csv.DictReader(csvfile, fieldnames=campos)
        return lector

def comprobar(fila):
    valor = fila[0]
    try:
        valor= float(valor)
        if float(valor).is_integer():
            valor = int(valor)
    except ValueError:
        sg.popup("No se puede guardar, el valor de monto debe ser un número", title="Error")
    ovalor = fila[1]
    if ovalor == str:
        ovalor = True
    if ovalor:
        return True
    else:
        sg.popup("No se puede guardar, debe poner la categoría", title="Error")

def leer_csv(nombre_archivo = 'datos.csv'):
    datos = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def mostrar_tabla():
    datos = leer_csv()
    layout2 = [
        [sg.Table(values=datos, headings=['Montos', 'Categorías', 'Fechas'])],
        [sg.Button("Cerrar")]
    ]
    window = sg.Window("Registro", layout2)
    while True:
        evento, diccionario = window.read()
        if evento == "Cerrar" or evento == WIN_CLOSED:
            break
    window.close()

def mostrar_resumen():
    datos = leer_csv()