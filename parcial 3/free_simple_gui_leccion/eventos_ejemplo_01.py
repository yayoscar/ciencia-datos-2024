import FreeSimpleGUI as sg

layout = [
    [sg.Text("nombre"),sg.Input(key="nombre")],
    [sg.Button("mostrar")]

]
window = sg.Window("mostrar nombre ingresado",layout,font=("Arial",20))

while True:
    event, values = window.read()
    if event == "mostrar":
        print(event,values)
        sg.popup(f"hola tu nombre es{values['nombre']}")
    elif event == sg.WIN_CLOSED:
        break

window.close()
