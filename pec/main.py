import FreeSimpleGUI as sg
from funciones import registrar_aporte, calcular_progreso

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Salir")]
]

window = sg.Window("Programa de Ahorro", layout)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Registrar aporte":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            aporte = float(values["APORTE"])
            registrar_aporte(aporte)
            sg.popup("Aporte registrado con éxito.")
        except ValueError:
            sg.popup_error("Por favor ingresa solo numeros.")
    elif event == "Ver progreso":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            progreso_texto = calcular_progreso(meta, semanas)
            sg.popup("esto llevas de la meta", progreso_texto)
        except ValueError:
            sg.popup_error("Por favor completa todos los campos correctamente.")

window.close()