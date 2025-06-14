import FreeSimpleGUI as sg
layout=[
[sg.Text("Nombre"), sg.Input(key="Nombre")],
[sg.Text("Edad"), sg.Input(key="EDAD")],
[sg.Button("Enviar"), sg.Button("Cancelar")]
    ]
window= sg.Window("formulario simple", layout, font=("Arial",20))
window.read()
window.close()
