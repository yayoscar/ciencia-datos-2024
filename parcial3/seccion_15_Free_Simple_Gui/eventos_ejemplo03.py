import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿Que quieresnhacer bby?")],
    [sg.Button("Saludar 1"),sg.Button("Saludar 2"), sg.Button("salir")],

]

window= sg.Window("Ejemplo 3, Multiples botones",layout,font=("Bodoni MT",20))

while True:
    evento,valores = window.read()
    if evento == "Saludar 1":
        sg.popup("hola ,este es un saludo del kbezuko")
    elif evento == "Saludar 2":
        sg.popup("hola, este es un saludo de aimep3")
    elif evento == sg.WIN_CLOSED or evento =="salir":
        break

window.close()