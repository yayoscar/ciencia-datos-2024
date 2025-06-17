import FreeSimpleGUI as sg

def main():
    layout = [
        [sg.Text('Temperatura (°C):')],
        [sg.Slider((0, 100), orientation='h', key='-TEMPERATURA-')],
        [sg.Button('Mostrar temperatura')]
    ]

    window = sg.Window('Control de temperatura', layout)

    while True:
        event, values = window.read()
        if event == 'Mostrar temperatura':
            temperatura = values['-TEMPERATURA-']
            if temperatura < 20:
                sg.popup(f"{temperatura}°C: Frío")
            elif 20 <= temperatura < 30:
                sg.popup(f"{temperatura}°C: Agradable")
            else:
                sg.popup(f"{temperatura}°C: Caliente")
        elif event == sg.WINDOW_CLOSED:
            break

    window.close()

if __name__ == '__main__':
    main()