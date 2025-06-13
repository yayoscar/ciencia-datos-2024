import FreeSimpleGUI as sg
layout=[
    [sg.Checkbox("¿Te gusta Python?", key="t_y_c")],
    [sg.Combo(["2.7", "3.6", "3.9", "3.11"], key="¿QUE COLOR USAS?")],
    [sg.Multiline(size=(30, 5), key="COMENTARIO")],
    [sg.Button("enviar")]
    ]

Window = sg.Window("Ejercicio02_Encuesta_Rápida", layout, font=("Arial", 20))

Window.read()
Window.close()

