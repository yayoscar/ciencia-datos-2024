import FreeSimpleGUI as sg


layaut = [
    [sg.Text("nombre"), sg.Input(key="NOMBRE")],
    [sg.Text("edad"), sg.Input(key="EDAD")],
    [sg.Button("envuar"), sg.Button("ENVIAR")],

]

window = sg.Window("formulario simple", layaut, font=("Arial",20))

window.read()
window.close()