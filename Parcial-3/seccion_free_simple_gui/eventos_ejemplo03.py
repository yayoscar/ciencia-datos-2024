import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿Que quieres hacer?")],
    [sg.Button("Saludar 1"), sg.Button("Saludar 2"), sg.Button("Salir")]
]

window = sg.Window("Ejemplo 3: Multiples botones",layout,font=("Arial",20))


while True:
    event,valores = window.read()
    if event == "Saludar 1":
        sg.popup("Hola este es un saludo")
    elif event == "Saludar 2":
        sg.popup("Este es otro saludo xd")
    elif event == sg.WIN_CLOSED or event == "Salir":
        break