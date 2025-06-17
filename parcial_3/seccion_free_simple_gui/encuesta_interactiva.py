import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese nombre: "),sg.Input(key="nombre")],
    [sg.Text("Ingrese edad: "),sg.Input(key="edad")],
    [sg.Text("Ingrese lenguaje favorito: "),sg.Combo["Python","Java","Java Script","C+"]],
    [sg.Checkbox("Acepto recibir emails",key='email')],
    [sg.Button("Enviar"),sg.Button("Cancelar")]
]

window = sg.Window("Mini encuesta interactiva",font=("Arial",20))

