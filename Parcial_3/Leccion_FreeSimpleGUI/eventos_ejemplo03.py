import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿Qué quieres hacer?",justification='None')],
    [sg.Button("Saludar 1"), sg.Button("Saludar 2"), sg.Button("Salir")]
]

window = sg.Window("Térmios y color", layout, font=('Arial', 20))
while True:
    eventos, valores = window.read()
    if eventos == "Salir" or eventos == sg.WIN_CLOSED:
        break
    elif eventos == "Saludar 1":
        sg.popup("Hola, este es un saludo", font=('Arial', 20))
    elif eventos == "Saludar 2":
        sg.popup("Este es otro saludo, holi", font=('Arial', 20))

window.close()