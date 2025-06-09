import FreeSimpleGUI as sg

layout = [
    [sg.Text('Nombre')],
    [sg.Input(key='-NOMBRE-')],
    [sg.Text('Edad')],
    [sg.Input(key='-EDAD-')],
    [sg.Button('Verificar')]
]


window = sg.Window('Verificar edad', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Verificar':
        try:
            edad = int(values['-EDAD-'])
            if edad >= 18:
                sg.popup(f'Hola {values["-NOMBRE-"]}, tu edad {edad} es válida')
            else:
                sg.popup(f'La edad {edad} no es válida. Debe ser mayor o igual a 18')
        except ValueError:
            sg.popup('La edad ingresada no es un número válido')

window.close()