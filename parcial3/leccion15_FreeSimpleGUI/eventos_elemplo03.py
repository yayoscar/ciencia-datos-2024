import FreeSimpleGUI as sg

from parcial3.ejemplo01 import layout, window

layout = [
    [sg.Text("¿Qué quieres hacer?")],
    [sg.Button("Saludar 1"),sg.Button("Saludar 2"), sg.Button("salir")]
]

window = sg.window("Ejemplo 3: Multiples botones",layout,font=("Arial",20))
while True:
    evento,valores = window.read()
    if evento == "Saludar 1":
        sg.popup("Hola este es un saludo")
    elif evento == "saludo 2":
        sg.popup("Este es otro saludo")
        elif evento == sg.WIN