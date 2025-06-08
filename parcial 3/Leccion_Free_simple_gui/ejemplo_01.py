import FreeSimpleGUI as sg


layout = [
    [sg.Text("hola mundo ")],[sg.Button("cerrar")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("aceptar terminos", key="T_Y_C")],
    [sg.Radio("opcion A","grupo1 ", key="a"),sg.Radio("opcion_B","grupo2",key="b") ],
    [sg.Combo(['axul', 'verde', 'rojo'], key="color")],
    [sg.Slider(range(0,100),orientation='h', key="SLIDER")],
    [sg.Multiline(size=(38,5),key="COMENTARIO")]
]

window = sg.Window("mi primer GUI", layout, font=('Arial', 30))

window.Read()
window.close()