import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED
from pygame.examples.sprite_texture import event

layout = [
    [sg.Text("Nombre"), sg.Input(key="nombre")],
    [sg.Button("Mostrar", button_color=('white', 'red'))]
]

window= sg.Window("Mostrar nombre ingresado", layout, font=('Arial', 20))

while True:
   event, values = window.read()
   if event == 'Mostrar':
       sg.popup(f"Hola, tu nombre es{values['nombre']}")
   elif event == WIN_CLOSED:
       break

window.close()