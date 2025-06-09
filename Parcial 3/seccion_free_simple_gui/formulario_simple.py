import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre: "), sg.Input(key='NOMBRE')],
    [sg.Text("Edad: "), sg.Input(key='EDAD')],
    [sg.Button("Enviar"), sg.Button('CANCELAR')]
]

window = sg.Window("Formulario simple", layout, font=("Arial", 20))

window.read()
window.close()