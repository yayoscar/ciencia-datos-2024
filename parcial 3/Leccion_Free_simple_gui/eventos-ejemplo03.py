import FreeSimpleGUI as sg


layaut = [
    [sg.Text("que quieres hacer")],
    [sg.Button("saludar 1 "), sg.Button("saludar 2"), sg.Button("salir")]

]

window = sg.Window("ejemplo 3 multiples botones", layaut,)

while True:
    evento, valores = window.read()
    if evento == "saludar 1 ":
        sg.popup("hola este es un saludo")
    elif evento == "saludar 2":
        sg.popup("este es otro saludo")
    elif evento == sg.WINDOW_CLOSED or evento== "salir":
        break

window.close()