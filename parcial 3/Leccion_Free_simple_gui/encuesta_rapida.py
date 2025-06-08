import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("¿Te gusta Python?", key="P")],
    [sg.Combo(["2.7", "3.6", "3.9", "3.11"], key="V")],
    [sg.Multiline("Comentarios...", key="C")],
    [sg.Button("Enviar")]
]

sg.Window("Encuesta", layout).read(close=True)