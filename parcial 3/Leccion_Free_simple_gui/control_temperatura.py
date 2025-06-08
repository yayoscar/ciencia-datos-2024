import FreeSimpleGUI as sg

layout = [
    [sg.Slider(range=(0, 100), orientation='h', key='T')],
    [sg.Button("Mostrar")]
]

sg.Window("Temperatura", layout).read(close=True)
