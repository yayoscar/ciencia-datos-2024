import FreeSimpleGUI as sg


layout=[
    [sg.Text("nombre"), sg.Input(key="nombre")],
    [sg.Button("mostrar")]

]
Window = sg.Window("Mostra nombre ingresado", layout,font=("Arial",20))
while True:
    event, values = Window.read()
    if event == 'Mostrar':
        sg.popup(f"hola!, Tu nombre es {values['nombre']}")
    elif event == sg.WIN_CLOSED:
        break
Window.close()