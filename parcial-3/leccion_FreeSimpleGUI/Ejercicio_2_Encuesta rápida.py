import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("¿Te gusta Python?", key="PYTHON")],
    [sg.Text("¿Qué versión usas?"), sg.Combo(["2.7", "3.6", "3.9", "3.11"], key="VERSION")],
    [sg.Text("Comentarios:"), sg.Multiline(size=(30, 5), key="COMENTARIOS")],
    [sg.Button("Enviar")]
]

window = sg.Window("Encuesta Rápida", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Enviar"):
        print(values)
        break

window.close()