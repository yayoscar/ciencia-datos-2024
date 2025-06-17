import FreeSimpleGUI as sg
import csv
from funciones import *

layout = [
    [sg.Text("Nombre del gasto:"), sg.InputText(key="nombre")],
    [sg.Text("Precio por unidad:"), sg.InputText(key="precio")],
    [sg.Text("Veces por semana:"), sg.InputText(key="veces")],
    [sg.Text("Tiempo en meses:"), sg.InputText(key="meses")],
    [sg.Button("Calcular"), sg.Button("Salir")],
    [sg.Text("Resultado:"), sg.Text("", size=(40, 1), key="resultado")]
]

ventana = sg.Window("Proyecto3: Calculadora de Gastos Hormiga ", layout,font=("Arial", 20))

while True:
    evento, valores = ventana.read()

    if evento == sg.WINDOW_CLOSED or evento == "Salir":
        break
    if evento == "Calcular":
        try:
            nombre = valores["nombre"]
            precio = float(valores["precio"])
            veces = int(valores["veces"])
            meses = int(valores["meses"])

            semanas = meses * 4
            total = precio * veces * semanas

            resultado = f"Total en {meses} meses: ${total:.2f} en {nombre}."
            ventana["resultado"].update(resultado)

            with open("datos.csv", "a", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow([nombre, precio, veces, meses, total])

        except ValueError:
            sg.popup("ingresa datos tus datos.")

ventana.close()