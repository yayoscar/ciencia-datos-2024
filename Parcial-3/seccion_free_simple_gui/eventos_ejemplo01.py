import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre"), sg.Input(key='nombre_usuario')],
    [sg.Button("Mostrar")]
]

window = sg.Window("Mostrar nombre ingresado", layout, font=("Arial",20))

while True:
    event,values = window.read()
    if event == 'Mostrar':
        print(event,values)
        sg.popup(f"Hola!, Tu Nombre es {values('nombre_usuario')}", font=("Arial",20))
    elif event == sg.WIN_CLOSED:
        break

window.close()