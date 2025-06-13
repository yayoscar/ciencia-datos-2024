import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese nombre:") , sg.Input(key="nombre")],
    [sg.Text("Ingrese edad"), sg.Input(key="edad")],
    [sg.Text("Lenguaje Favorito:"),sg.Combo(["Python","Javascript","C++","Go","COMBO"], key="lenguaje")],
    [sg.Checkbox("Acepto recibir emails",key="email")],
    [sg.Button("Enviar"),sg.Button("Cancelar")]
]
