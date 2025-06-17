import FreeSimpleGUI as sg
from FreeSimpleGUI import Radio

layout = [
    [sg.Text("holamundo"),sg.Button('cerrar')],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar terminos",key="t_y_c")],
    [sg.Radio("Opcion A","GRUPO1",key="A"), sg.Radio("Opcion B", "GRUPO 1",key="B")],
    [sg.Combo(["Rojo", "Verde", "Azul"], key="COLOR")],
    [sg.Slider(range=(1, 100), orientation='h', key='SLIDER')],
    [sg.Multiline(size=(30,5), key="COMENTARIO")],


 ]
Window = sg.Window("ejemplo01 - Mi primer GUI",layout,font=('Arial',20))


Window.read()
Window.close()
