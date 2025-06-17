import FreeSimpleGUI as simplegui

layout=[
    [simplegui.Text("ingrese su nombre")],
    [simplegui.Input(key="nombre")],
    [simplegui.Checkbox("aceptar terminos",key="t_y_c")],
    [simplegui.Radio("si","Grupo 1",key="a"),simplegui.Radio("no","grupo B",key="b")],
    [simplegui.Combo(("rojo","azul","verde"), key="color")],
    [simplegui.Slider(range=(1,100),orientation="h",key="Slider")],
    [simplegui.Multiline(size=(30,5), key="comentarios")],
    [simplegui.Button("cerrar")],
]
while True:
    window= simplegui.Window("ventana",layout,font=("High Tower Text",23))


    window.read()
    window.close()
