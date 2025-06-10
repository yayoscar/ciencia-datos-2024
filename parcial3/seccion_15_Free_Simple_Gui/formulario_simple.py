import FreeSimpleGUI as sg

layaout= [
    [sg.Text("edad: "), sg.Input(key="nombre")],
    [sg.Text("Edad: "), sg.Input(key="Edad")],
    [sg.Button("eviar: "), sg.Button("cancelar")]
]

window = sg.Window("Formulario simple", layaout)