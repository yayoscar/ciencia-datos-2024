import FreeSimpleGUI as sg
from funciones import calcular_ahorro, guardar_datos

layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="NOMBRE")],
    [sg.Text("Precio por unidad:"), sg.Input(key="PRECIO")],
    [sg.Text("Veces por semana:"), sg.Input(key="VECES")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Button("Calcular ahorro"), sg.Button("Salir")]
]

window = sg.Window("Calculadora de Gastos Hormiga", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    if event == "Calcular ahorro":
        try:
            nombre = values["NOMBRE"]
            precio = float(values["PRECIO"])
            veces = int(values["VECES"])
            meses = int(values["MESES"])
            total = calcular_ahorro(precio, veces, meses)
            guardar_datos(nombre, precio, veces, meses, total)
            sg.popup(f"Puedes ahorrar ${total:,.2f} si dejas de consumir '{nombre}' durante {meses} meses.")
        except ValueError:
            sg.popup("Por favor, ingresa valores numéricos válidos en precio, veces y meses.")

window.close()
