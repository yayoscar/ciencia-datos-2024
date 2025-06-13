import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre:"),sg.Input(key="NOMBRE")],
    [sg.Button("Mostrar")]
]

window = sg.Window("Evento 01",layout)