import FreeSimpleGUI as sg

layout = [
[sg.Text("Meta de ahorro:"), sg.Input(key="META")],
[sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
[sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
[sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("PROYECTO_PEC", layout, font=("Arial", 20))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event ==


window.close()