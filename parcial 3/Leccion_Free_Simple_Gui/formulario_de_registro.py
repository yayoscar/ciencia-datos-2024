import FreeSimpleGUI as sg
layout = [
    [sg.Text('Nombre'), sg.Input(key='NOMBRE')],
    [sg.Text('Apellido'), sg.Input(key='APELLIDO')],
    [sg.Text('E-mail'), sg.Input(key='EMAIL')],
    [sg.Button('Enviar', button_color='dark blue'), sg.Button('Limpiar', button_color='dark blue')]
]
ventana = sg.Window('Formulario de registro', layout)
ventana.read()
ventana.close()