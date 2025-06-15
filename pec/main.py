import FreeSimpleGUI as sg

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="meta")],
    [sg.Text("Número de semanas:"), sg.Input(key="semanas")],
    [sg.Text("Aporte actual:"), sg.Input(key="aporte")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Salir")]
]
ventana = sg.Window("Meta de ahorro", layout)

while True:
    event, values = ventana.read()
    if event == sg.WIN_CLOSED or event == "Salir":
        break

ventana.close()