import FreeSimpleGUI as sg
layout=[
    [sg.Slider(range=(0, 100), orientation='h', key="SLIDER")],
    [sg.Button("seleccionar temperatura")]
]

Window = sg.Window("Ejercicio03_Control_temperatura", layout, font=("arial", 20))
Window.read()
Window.close()