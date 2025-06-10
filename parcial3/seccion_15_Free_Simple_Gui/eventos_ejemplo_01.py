import FreeSimpleGUI as sg
from FreeSimpleGUI import popup

layout = [
    [sg.Text("nombre"), sg.Input(key="nombre", background_color= 'lightpink')],
    [sg.Button("Mostrar", button_color=("purple"))],

]
window = sg.Window("mostrar nombre ingresado", layout,font=("Arial",20))

while True:
    event , values = window.Read()
    if event =='Mostrar':
        sg,popup(f"Hola!, tu nombre es{values['nombre']}")
    elif event == sg.WIN_CLOSED:
        break

window.close()