import FreeSimpleGUI as sg
layout= [
    [sg.Input(key='NUM1', size=5), sg.Text('+'),sg.Input(key='NUM2', size=5), sg.Text('= ??')],
    [sg.Button("Sumar")]
]
ventana = sg.Window("Calculadora de suma simple", layout, font=("Arial",20))
ventana.read()
ventana.close()
