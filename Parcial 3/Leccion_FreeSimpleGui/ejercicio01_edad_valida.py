import FreeSimpleGUI as sg

def main():
    layout = [
        [sg.Text('Nombre:'), sg.Input(key='-NOMBRE-')],
        [sg.Text('Edad:'), sg.Input(key='-EDAD-')],
        [sg.Button('Verificar')]
    ]

    window = sg.Window('Verificación de edad', layout)

    while True:
        event, values = window.read()
        if event == 'Verificar':
            try:
                edad = int(values['-EDAD-'])
                nombre = values['-NOMBRE-']
                if edad >= 18:
                    sg.popup(f"{nombre}, eres mayor de edad.")
                else:
                    sg.popup(f"{nombre}, eres menor de edad.")
            except ValueError:
                sg.popup_error("Por favor, ingresa una edad válida.")
        elif event == sg.WINDOW_CLOSED:
            break

    window.close()

if __name__ == '__main__':
    main()