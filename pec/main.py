import FreeSimpleGUI as sg
from datetime import datetime
import os

from pec.funciones import datos_csv
from datetime import datetime

layout = [
    [sg.Text("Proyecto pec:",pad=(300,20),font=('Arial',40))],
    [sg.Text(" Monto del gasto :",pad=(0,20),font=('Arial',20)),sg.Input(key='MONTO',size=(22,0))],
    [sg.Text("    Categoria:  "),sg.Combo(['Comida','Transporte','Electricidad'],size=(21,0),pad=(40,10),key='CATEGORIA')],
    [sg.Text(' Fecha (opcional):',pad=(0,20)),sg.Input(key='FECHA',size=(22,0))],
    [sg.Button("Guardar gasto",button_color=('black','blue')),sg.Button("Ver resumen",button_color=('black','green')),sg.Button('Ver registros',button_color=('black','yellow')),sg.Button('Salir',button_color=('black','red'))]


]

window = sg.Window("Proyecto pec", layout,font=('Arial',20))

archivo_csv = 'datos.csv'
datos_usuario = ['Monto del gasto','Categoria','Fecha(opcional)']


while True:
    evento,values = window.read()
    if evento == sg.WIN_CLOSED or evento == 'Salir':
        break
    if evento == 'Guardar gasto':
        monto = values ['MONTO']
        categotia = values ['CATEGORIA']
        fecha = values['FECHA'] if values['FECHA'] else datetime.today().strftime('%Y-%m-%d')
        if not monto or not categotia:
            sg.popup('Ingresa un monto y una categoria')
            continue
        try:
            float(monto)
        except ValueError:
            sg.popup('El monto debe ser un numero valido')
            continue
        datos = [fecha,categotia,monto]
        datos_csv(archivo_csv, datos, datos_usuario)
        sg.popup('Datos guardados correctamente')
    if evento == "Ver registros":
        if os.path.isfile(archivo_csv):
            with open(archivo_csv, newline='', encoding='utf-8') as f:
                contenido = f.read()
            sg.popup_scrolled("Registros guardados", contenido)
        else:
            sg.popup("No hay registros guardados aún.")






      








        
        




window.close()

