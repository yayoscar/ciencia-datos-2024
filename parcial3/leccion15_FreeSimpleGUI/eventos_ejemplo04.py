import FreeSimpleGUI as sg
layout = [
    [sg.Text("Ingrese nombre:"),sg.Input(key="nombre")],
    [sg.Text("Ingrese su edad:"),sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito:"),sg.combo(["python","javascrip","C++","Go","java"])]
]