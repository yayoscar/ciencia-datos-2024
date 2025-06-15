import FreeSimpleGUI as sg
layout = [
    [sg.Text("hola mundo"), sg.Button("Cerrar")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar términos", key="t_y_c")],
    [sg.Radio("Opcion A", "GRUPO1", key="a"), sg.Radio("Opcion B", "GRUPO1", keys="b")]
]

window = sg.Window("Ejemplo01 - Mi primera GUI", layout,font=('Arial',20))

window.read()
window.close()