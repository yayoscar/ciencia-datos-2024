import FreeSimpleGUI as sg
layout=[
    [sg.Imput(key="numero1"), sg.Text("+"), sg.Input(key="numero2"), sg.Text("=")],
    [sg.Button("Sumar")]
]

window = sg.window( "Ejercicio05_Calculadora_simple", layout,font=("Arial",20))
window.read()
window.close()
