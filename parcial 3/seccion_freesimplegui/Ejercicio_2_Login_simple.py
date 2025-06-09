import FreeSimpleGUI as sg


layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='-USUARIO-')],
    [sg.Text('Contraseña')],
    [sg.Input(password_char='*', key='-CONTRASEÑA-')],
    [sg.Button('Ingresar')]
]


window = sg.Window('Login', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ingresar':
        usuario = values['-USUARIO-']
        contraseña = values['-CONTRASEÑA-']
        if usuario == 'admin' and contraseña == '1234':
            sg.popup('Acceso concedido')
        else:
            sg.popup('Usuario o contraseña incorrectos')


window.close()