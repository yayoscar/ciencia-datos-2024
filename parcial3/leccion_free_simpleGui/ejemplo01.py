import FreeSimpleGUI as sg
from FreeSimpleGUI import Multiline

#layout; significa diseño, es el diseño
layout=[
    [sg.Text("Hola mundo")],
    [sg.Button("Cerrar")],
    [sg.Input(key="Nombre")],
    [sg.Checkbox("Aceptar terminos", key="t_y_c")],
    [sg.Radio("opcion A","Grupo01",key="a"), sg.Radio ("opcion B", "Grupo02", key="b")],
    [sg.Combo(["Rojo","Verde","Azul"],key="COLOR")],
    [sg.Slider(range=(1, 100), orientation='h',key='SLIDER')],

]

window = sg.Window("Mi primera GUI", layout,font=("arial",18))
#front0 ; sirve para la letra, la fuente
window.read()
window.close()
