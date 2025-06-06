import FreeSimpleGUI as sg
layout= [
    [sg.Slider(range=(10, 100), orientation='h', key= 'SLIDER')],
    [sg.Button('Temperatura')]
]
ventana = sg.Window('Control de temperaturas', layout)
ventana.read()
ventana.close()