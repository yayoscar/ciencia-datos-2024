import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Enviar"),sg.Button("Cancelar")]
]

window = sg.Window("Formulario Simple",layout,font=("Arial",20))

window.read()
window.close()
