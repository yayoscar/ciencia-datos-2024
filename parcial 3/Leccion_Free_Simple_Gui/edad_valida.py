import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED

layout = [
    [sg.Text("Nombre: "), sg.Input(key='nombre')],
    [sg.Text("Edad: "), sg.Input(key='edad')],
    [sg.Button('Verificar')]
]
window = sg.Window("Ejemplo01 - Mi primer GUI", layout, font=("Arial", 20), background_color='#8EC6B5')

while True:
    evento, valor = window.read()
    if evento == 'Verificar':
        edad = valor['edad']
        nombre = valor['nombre']
        if int(edad) >= 18:
            sg.popup(f"{nombre. capitalize()}, eres mayor de edad")
        else:
            sg.popup(f"{nombre.capitalize()}, eres menor de edad")
    elif evento == WIN_CLOSED:
        break
window.close()