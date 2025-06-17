import FreeSimpleGUI as sg


layout=[
       [sg.Text("nombre"), sg.Input(key="nombre")],
       [sg.Text("edad"), sg.Input(key="edad")],
       [sg.Button("enviar"),sg.Button("cancelar")]
]

window= sg.Window("Formulario simple",layout,font=("High Tower Text",23))


window.read()
window.close()