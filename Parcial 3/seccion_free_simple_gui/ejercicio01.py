import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre: "), sg.Input(key='NOMBRE')],
    [sg.Text("Apellido: "), sg.Input(key='APELLIDO')],
    [sg.Text("Email: "), sg.Input(key='EMAIL')],
    [sg.Button("Enviar"), sg.Button("Limpiar")]
]

window = sg.Window("Formulario simple", layout, font=("Arial", 20))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Enviar":
        sg.popup("Datos enviados",
                 f"Nombre: {values['NOMBRE']}\n"
                 f"Apellido: {values['APELLIDO']}\n"
                 f"Email: {values['EMAIL']}")

    elif event == "Limpiar":
        window['NOMBRE'].update("")
        window['APELLIDO'].update("")
        window['EMAIL'].update("")

window.close()