import FreeSimpleGUI as sg

layout = [
    [sg.Text("QUIERES JUGAR FREE FIRE 2?"),sg.Button("cerrar")],
    [sg.Input(key="nombre")],
    [sg.Checkbox("Aceptar terminos y condiciones", key="t_y_c")],
    [sg.Radio("Clasico", "GRUPO1", key="a"),sg.Radio("Clasificatoria", "GRUPO2", key="b")],
    [sg.Combo(["SOLO","DUO","ESCUADRA"],key="EQUIPO")],
    [sg.Slider(range=(1, 100), orientation='h', key='SLIDER')],
    [sg.Multiline(size=(30, 5), key="COMENTARIO")]

]


window = sg.Window("ejemplo01 - Mi primer GUI",layout,font=('Arial',20))

window.read()
window.close()