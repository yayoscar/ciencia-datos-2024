import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre"),sg.Input(key="nombre")],
    [sg.Button("Mostrar")]

]

window= sg.Window("Mostrar nombre ingresado",layout,font=("Arial",20))

while True:
    event, values = window.read()
    if event == 'Mostrar':
        sg.popup(f"tu  nombre es {values['nombre']}")
    elif event == sg.WIN_CLOSED:
        break

window.close()


