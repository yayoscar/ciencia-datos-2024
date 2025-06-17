import FreeSimpleGUI as sg

layout = [
    [sg.Text("nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Enviar"),sg.Button("CANCELAR")]
]

Window = sg.Window("Formulario Simple", layout, font=("Arial",20))

Window.read()
Window.close()

