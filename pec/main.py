import FreeSimpleGUI as sg

layout = [
    [sg.Text("Proyecto pec:",pad=(300,20),font=('Arial',40))],
    [sg.Text(" Monto del gasto :",pad=(0,20),font=('Arial',20)),sg.Input(key='MONTO',size=(22,0))],
    [sg.Text("    Categoria:  "),sg.Combo(['Comida','Transporte','Electricidad'],size=(21,0),pad=(40,10),key='CATEGORIA')],
    [sg.Text(' Fecha (opcional):',pad=(0,20)),sg.Input(key='FECHA',size=(22,0))],
    [sg.Button("Guardar gasto",button_color=('black','blue')),sg.Button("Ver resumen",button_color=('black','green')),sg.Button('Salir',button_color=('black','red'))]


]

window = sg.Window("Proyecto pec", layout,font=('Arial',20))

while True:
    eventos,values = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Salir':
        break
    if eventos == 'Guardar gasto':
        




window.close()

