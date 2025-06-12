import FreeSimpleGUI as sg
from pec.funciones import datos_csv

layout = [
    [sg.Text("Proyecto pec:",pad=(300,20),font=('Arial',40))],
    [sg.Text(" Monto del gasto :",pad=(0,20),font=('Arial',20)),sg.Input(key='MONTO',size=(22,0))],
    [sg.Text("    Categoria:  "),sg.Combo(['Comida','Transporte','Electricidad'],size=(21,0),pad=(40,10),key='CATEGORIA')],
    [sg.Text(' Fecha (opcional):',pad=(0,20)),sg.Input(key='FECHA',size=(22,0))],
    [sg.Button("Guardar gasto",button_color=('black','blue')),sg.Button("Ver resumen",button_color=('black','green')),sg.Button('Salir',button_color=('black','red'))]


]

window = sg.Window("Proyecto pec", layout,font=('Arial',20))

archivo_csv = 'datos.csv'
datos_usuario = ['Monto del gasto','Categoria','Fecha(opcional)']

while True:
    evento,values = window.read()
    if evento == sg.WIN_CLOSED or evento == 'Salir':
        break
    if evento == 'Guardar gasto':
        datos = [values['MONTO'],values['CATEGORIA'],values['FECHA']]
        datos_csv(archivo_csv,datos, datos_usuario)
        sg.popup('Datos guardados correctamente')






        
        




window.close()

