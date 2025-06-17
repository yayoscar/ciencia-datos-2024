import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿que quieres hacer?")],
    [sg.Button("saludar1"),sg.Button("saludar2"),sg.Button("salir")]

]

window = sg.Window("ejemplo 3:multiples botones", layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "saludar 1:":
        sg.popup("hola este es un saludo")
    elif evento == "saludar2":
        sg.popup("este es otro saludo")
    elif evento == sg.WIN_CLOSED or evento =="salir":
        break

window.close()