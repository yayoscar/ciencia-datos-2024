import  FreeSimpleGUI as sg
from FreeSimpleGUI import Input

layaout = [
    [sg.Text("hola mundo"), sg.Button("cerrar")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar terminos",key="t_y_c")],
    [sg.Radio("opccion A", "GRUPO 1",key="a"), sg.Radio("opccion B", "GRUPO1",key="b")],
    [sg.Combo(["Rosa","Morado","Azul"], key="COLOR")],
    [sg.Slider(range=(1, 100,2), orientation='h', key='SLIDER')],
    [sg.Multiline(size=(30, 5), key="COMENTARIO")]

]

window = sg.Window("Ejemplo 01 - Mi primer GUI",layaout,font=('Bodoni MT',10))

window.read()
window.close()