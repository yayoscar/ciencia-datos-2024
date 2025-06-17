import FreeSimpleGUI as sg

def main():
    layout = [
        [sg.Text('Usuario:'), sg.Input(key='-USUARIO-')],
        [sg.Text('Contraseña:'), sg.Input(password_char='*', key='-CONTRASEÑA-')],
        [sg.Button('Ingresar')]
    ]

    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()
        if event == 'Ingresar':
            usuario = values['-USUARIO-']
            contrasena = values['-CONTRASEÑA-']
            if usuario == "admin" and contrasena == "1234":
                sg.popup("Bienvenido, acceso concedido.")
            else:
                sg.popup_error("Usuario o contraseña incorrecta.")
        elif event == sg.WINDOW_CLOSED:
            break

    window.close()