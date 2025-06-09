import FreeSimpleGUI as sg

layout = [
    [sg.Text("Usuario:"), sg.Input(key="USUARIO")],
    [sg.Text("Contraseña:"), sg.Input(password_char="*", key="CLAVE")],
    [sg.Button("Ingresar")]
]

window = sg.Window("Login", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Ingresar":
        if values["USUARIO"] == "admin" and values["CLAVE"] == "1234":
            sg.popup("Acceso concedido.")
        else:
            sg.popup("Usuario o contraseña incorrectos.")

window.close()