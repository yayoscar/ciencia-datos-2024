import FreeSimpleGUI as sg

layout = [
    [sg.Text("ingrese el nombre:"),sg.Input(key="nombre")],
    [sg.Text("ingrese edad:"), sg.Input(key="edad")],
    [sg.Text("lenguaje favorito:"), sg.Combo["lenguaje", 'java', 'javascript', 'C', 'Python', 'C++']],
    [sg.Checkbox("acepto recibir emails", key="email")],
    [sg.Button("enviar"), sg.Button("cambiar")]
]

window = sg.Window("mini encuesta interactiva", layout, font=("Arial", 30))

while True:
