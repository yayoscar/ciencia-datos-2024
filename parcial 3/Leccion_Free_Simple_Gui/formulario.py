import FreeSimpleGUI as sg
layout = [
    [sg.Text("Nombre:"), sg.Input(key="nombre")],
    [sg.Text("Edad:"), sg.Input(key="edad")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]
ventana = sg.Window('Formulario', layout)
ventana.read()
ventana.close()

