import FreeSimpleGUI as sg

layout = [
    [sg.Text("Monto del gasto"),sg.Input(key='MONTO')],
    [sg.Text("Categoria:"),sg.Combo(['Comida','Transporte','Electricidad'],key='CATEGORIA')],
    [sg.Text('Fecha (opcional):'),sg.Input(key='FECHA')],
    [sg.Button("Guardar gasto"),sg.Button("Ver resumen")]

]

window = sg.Window("Proyecto pec", layout,font=('Arial',12))