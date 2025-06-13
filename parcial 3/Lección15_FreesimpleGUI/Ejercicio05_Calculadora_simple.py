import FreeSimpleGUI as sg
layout=[
    [sg.Input(key="numero1"), sg.Text("+"), sg.Input(key="numero2"), sg.Text("=")],
    [sg.Button("Sumar")]
]

Window = sg.Window("Ejercicio05_Calculadora_simple", layout,font=("Arial",20))
Lectura = Window.read()
print(Lectura)
Window.close()