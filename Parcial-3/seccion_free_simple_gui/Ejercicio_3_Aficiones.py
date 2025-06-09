import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox('Música', key='-MUSICA-'), sg.Checkbox('Lectura', key='-LECTURA-'), sg.Checkbox('Deporte', key='-DEPORTE-')],
    [sg.Button('Mostrar selección')],
    [sg.Text('', key='-SELECCION-')]
]

window = sg.Window('Aficiones', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Mostrar selección':
        hobbies = []
        if values['-MUSICA-']:
            hobbies.append('Música')
        if values['-LECTURA-']:
            hobbies.append('Lectura')
        if values['-DEPORTE-']:
            hobbies.append('Deporte')
        seleccion = ', '.join(hobbies) or 'Ninguno'
        sg.popup("Hobbies seleccionados",", ".join(hobbies) or "Ninguno")

window.close()