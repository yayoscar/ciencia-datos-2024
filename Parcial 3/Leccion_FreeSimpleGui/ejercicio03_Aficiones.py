import FreeSimpleGUI as sg

def main():
    layout = [
        [sg.Checkbox('Leer', key='-LEER-')],
        [sg.Checkbox('Escuchar música', key='-MUSICA-')],
        [sg.Checkbox('Caminar', key='-CAMINAR-')],
        [sg.Button('Mostrar selección')]
    ]

    window = sg.Window('Aficiones', layout)

    while True:
        event, values = window.read()
        if event == 'Mostrar selección':
            hobbies = [hobby for hobby, seleccionado in values.items() if seleccionado]
            hobbies_texto = {
                '-LEER-': 'Leer',
                '-MUSICA-': 'Escuchar música',
                '-CAMINAR-': 'Caminar'
            }
            seleccionados = [hobbies_texto[hobby] for hobby in hobbies]
            if seleccionados:
                sg.popup(f"Hobbies seleccionados: {', '.join(seleccionados)}")
            else:
                sg.popup("No has seleccionado ningún hobby.")
        elif event == sg.WINDOW_CLOSED:
            break

    window.close()

if __name__ == '__main__':
    main()