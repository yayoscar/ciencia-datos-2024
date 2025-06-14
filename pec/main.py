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
    if event in (sg.WINDOW_CLOSED, "Salir"):
        break

    if event == "Calcular ahorro":
        try:
            nombre = values["NOMBRE"]
            precio = float(values["PRECIO"])
            veces = int(values["VECES"])
            meses = int(values["MESES"])

            ahorro = calcular_ahorro(nombre, precio, veces, meses)

            guardar_datos(nombre, precio, veces, meses, ahorro)

            sg.popup(f"Podrías ahorrar ${ahorro:.2f} si evitas '{nombre}' por {meses} meses.")
        except Exception as e:
            sg.popup("Error:", str(e))

window.close()
