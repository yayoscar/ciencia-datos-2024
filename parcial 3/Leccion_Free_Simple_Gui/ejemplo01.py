import FreeSimpleGUI as sg

layout = [
    [sg.Text("Hola mundo"),sg.Button('cerrar')],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar terminos", key="t_y_c")],
    [sg.Radio("Opcion A","Group1!", key="a"), sg.Radio("Opcion B", "Group1", key="b")],
    [sg.Combo(["Rojo", "Verde", "Azul"], key="COLOR")],
    [sg.Slider(range=(1, 100), orientation='h', key='SLIDER')],
    [sg.Multiline(size=(30, 5), key="COMENTARIO")]

]


window= sg.Window( "Ejemplo01 - Mi primer GUI", layout, font=("arial",20))

window.read()
