import FreeSimpleGUI as sg

layout = [
    [sg.Text("Hola mundo"),sg.Button("Cerrar")],
    [sg.Input(key="Nombre")],
    [sg.Checkbox("Aceptar terminos", key="t_y_c")],
    [sg.Radio("Opcion A","GRUPO1",key="a"),sg.Radio("Opcion B","GRUPO1",key="b")],
    [sg.Combo(["Rojo","Verde","Azul"],key="COLOR")],
    [sg.Slider(range=(1,100), orientation='h',key='SLIDER')]

]

window = sg.Window("Ejemplo01 - Mi primer GUI",layout,font=('Britannic Negrita',30))

window.read()
window.close()
