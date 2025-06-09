import FreeSimpleGUI as sg

layout= [
    [sg.Text("Que quieres hacer?")],
    [sg.Button("Saludar 1"),sg.Button("Saludar 2"),sg.Button("Salir")]
]

window = sg.Window("Ejemplo 3:Multiples saludos",layout,font=("Arial",20))

while True:
    eventos,valores = window.read()
    if eventos == "Saludar 1":
        sg.popup("Hola, este es un saludo")
    elif eventos == "Saludar 2":
        sg.popup("Hola, este es otro saludo")
    elif eventos == sg.WIN.CLOSED or eventos == "Salir":
        break