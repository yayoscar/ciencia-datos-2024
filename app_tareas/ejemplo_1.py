import FreeSimpleGUI as sg

layout = [
    [sg.Text("hola mundo")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar terminos", key="t_y_c")],
    [sg.Radio("opcion A", "Grupo01", key="a"), sg.Radio("opcion B", "grupo02", key="b")],
    [sg.Combo(["rosado", "azul", "amarillo"], key="COLOR")],
    [sg.Slider(range=(1, 100), orientation='h', key="SLIDER")],
    [sg.Multiline(size=(30, 50), key="COMENTARIO")]
]
Window = sg.Window(" - Mi primer Gui", layout,font=('Blackadder ITC',20))
#font: sirve para cambiar las letras de la fuente
Window.read()
Window.close()