import FreeSimpleGUI as sg

layout=[
    [sg.Input(key="numero1"), sg.Text("+"), sg.Input(key="numero2"),sg.Text("=  ")],
    [sg.Button("sumar")]
]

window= sg.Window("Ejercicio 5: calculadora de suma simple", layout, font=("Arial",20))

window.Read()
window.close()