import FreeSimpleGUI as sg

layout=[
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="NOMBRE")],
    [sg.Text("Precio por unidad"), sg.Input(key="PRECIO")],
    [sg.Text("Veces por semana:"), sg.Input(key="VECES")],
    [sg.Text("Meses:"), sg.Input(key="VECES")],
    [sg.Button("Calcular ahorro")]


]

Window = sg.Window("Proyecto 3: Calcular ahorro",layout,font=("Arial, 12"))
Window.read()
Window.close()