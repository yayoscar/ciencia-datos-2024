import FreeSimpleGUI as sg

layout = [
    [sg.Text("Hola mundo"),sg.Button("Cerrar")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Acepatr terminos", key="t_y_c")],
    [sg.Radio("Opcion A", "GRUPO1", key="a"), sg.Radio("Opcion B", "GRUPO1", key="b")],
    [sg.Combo(["Rojo", "Verde", "Azul"], key="COLOR")],
    [sg.Slider(range=(1, 100), orientation= 'h', key='SLIDER')],
    [sg.Multiline(size=(30, 5), key="COMENTARIO")]

]

window = sg.Window("Ejemple01 - Mi primer GUI", layout,font=('Arial',20))

window.read()
window.close()

