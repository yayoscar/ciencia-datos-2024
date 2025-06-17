import FreeSimpleGUI as sg
from funciones import registrar_aporte, mostrar_progreso, reiniciar_progreso

layout = [
    [sg.Text("Meta total ($):"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte de esta semana ($):"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Reiniciar progreso")]
]

window = sg.Window("Reto de Ahorro Personalizado", layout)

while True:
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "Registrar aporte":
        try:
            m = int(valores["META"])
            s = int(valores["SEMANAS"])
            a = int(valores["APORTE"])
            registrar_aporte(m, s, a)
            window["APORTE"].update("")

        except ValueError:
            sg.popup("Por favor, ingresa solo números válidos en todos los campos.")

    elif evento == "Ver progreso":
        mostrar_progreso()

    elif evento == "Reiniciar progreso":
        reiniciar_progreso()
        window["META"].update("")
        window["SEMANAS"].update("")
        window["APORTE"].update("")

window.close()
