import FreeSimpleGUI as sg

layout = [
    [sg.Button("Rock, Pop, Jazz, Clásica.")],
    [sg.Button("Confirmar")]
]

ventana =  sg.Window("Selector de género musical. ",layout,font=("Arial",20))

ventana.read()
ventana.close()