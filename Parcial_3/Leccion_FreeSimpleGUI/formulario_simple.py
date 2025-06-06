import FreeSimpleGUI as sg
layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]
ventana = sg.Window('Formulario simple', layout)
ventana.read()
ventana.close()

