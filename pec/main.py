import FreeSimpleGUI as sg
layout = [
[sg.Text("Meta de ahorro:"), sg.Input(key="META")],
[sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
[sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
[sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]


window = sg.Window("Reto de Ahorro", layout)


while True:
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == "Iniciar":
        meta = float(valores["meta"])
        semanas = int(valores["semanas"])
