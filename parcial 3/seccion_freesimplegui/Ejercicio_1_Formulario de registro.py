import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Apellido:"), sg.Input(key="APELLIDO")],
    [sg.Text("Email:"), sg.Input(key="EMAIL")],
    [sg.Button("Enviar"), sg.Button("Limpiar")]
]

window = sg.Window("Formulario de Registro", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Enviar"):
        print(values)
        break
    elif event == "Limpiar":
        window["NOMBRE"].update("")
        window["APELLIDO"].update("")
        window["EMAIL"].update("")

window.close()
