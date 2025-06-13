import FreeSimpleGUI as sg
layout = [
    [sg.Text("¿Qué quieres hacer??")],
    [sg.Button("Saludar 1"),sg.Button("Saludar 2"),sg.Button("Salir")]
]

window = sg.Window("Ejemplo 3: Multiples botones",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "Saludar 1":
        sg.popup("Hola,este es un saludo")
    elif evento == "Saludar 2":
        sg.popup("Este es otro saludo :)")
    elif evento == sg.WIN_CLOSED or evento == "Salir":
        break

window.close()