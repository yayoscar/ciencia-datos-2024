
import FreeSimpleGUI as sg
layout=[
[sg.Radio("Opcion A", "GRUPO1", key="a"), sg.Radio("Opcion B", "GRUPO2", key="b"), sg.Radio("Opcion C", "GRUPO3", key="C"), sg.Radio("Opcion D", "GRUPO4", key="D")],
    [sg.Button("Rock"), sg.Button("Pop"), sg.Button("Jazz"), sg.Button("Clásica")],
    [sg.Button("confirmar")]
]

Window = sg.Window("Ejercicio04_Selector_Genero_Musical", layout, font=("Arial", 20))
Window.read()
Window.close()