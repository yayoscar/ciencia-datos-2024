import FreeSimpleGUI as sg
from funciones import registrar_aporte, calcular_progreso

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("Programa de Ahorro", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    try:
        meta = float(values["META"])
        semanas = int(values["SEMANAS"])
    except ValueError:
        sg.popup_error("Por favor ingresa una meta y número de semanas válidos.")
        continue

    if event == "Registrar aporte":
        try:
            aporte = float(values["APORTE"])
            registrar_aporte(aporte)
            sg.popup(" Aporte registrado.")
        except ValueError:
            sg.popup_error("Por favor ingresa un número válido en 'Aporte'.")

    elif event == "Ver progreso":
        mensaje = calcular_progreso(meta, semanas)
        sg.popup("Progreso", mensaje)

window.close()
