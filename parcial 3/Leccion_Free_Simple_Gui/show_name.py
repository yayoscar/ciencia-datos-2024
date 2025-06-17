import FreeSimpleGUI as sg

from Leccion_Free_Simple_Gui.ejemplo01 import window
from Leccion_Free_Simple_Gui.eventos_ejemplo01 import values

layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Button("Mostrar")]
]

window = sg.Window("Nombre", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Mostrar":
        sg.popup(f"Tu nombre es: {values['']}")