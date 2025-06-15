import FreeSimpleGUI

from parcial3.ejemplo01 import window

layout=[
    [sg.Text("Nombre"),sg.Input(key="nombre")],
    [sg.Button("Mostrar")]
]
window = sg.window( "Mostrar nombre ingresado",layout,font=("Arial",20))
