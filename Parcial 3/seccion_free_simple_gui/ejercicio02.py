import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("¿Te gusta Python?", key="t_y_c")],
    [sg.Text("¿Qué versión usas?"),sg.Combo(["2.7", "3.6", "3.9", "3.11"], key="version")],
    [sg.Multiline(size=(30, 5), key="comentario")],
    [sg.Button("Enviar")]
]

window = sg.Window("Encuesta rápida", layout, font=("Arial", 20))

window.read()
window.close()