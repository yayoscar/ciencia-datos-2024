import FreeSimpleGUI as sg

layout=[
    [sg.Text("Nombre"),sg.Input(key="nombre")],
    [sg.Button("Mostrar")]
]

window = sg.Window("Mostrar el nombre ingresado",layout,font=("Arial",20))

while True:
    event, values = window.read()
    if event == 'mostrar':
        print(event,values)
        sg.popup(f"Hola!, Tu nombre es {values['nombre']}",font=("Arial",20))
    elif event == sg.WIN_CLOSED:
        break

window.close()