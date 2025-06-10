import FreeSimpleGUI as sg
import csv
import os
import funciones
from pec.funciones import guardar_gastos

layout= [
    [sg.Text("Monto del gasto: "), sg.Input(key="MONTO")],
    [sg.Text("Categoria"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional)"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen")],
    [sg.Text('', size=(40,1), key='-STATUS-')]

]

ventana = sg.Window("Registro de Gastos y Categorias",layout,font=("Comic Sans",20))

while True:
    event, values = ventana.read()
    if event in (sg.WIN_CLOSED, 'Salir'):
        break
    elif event == 'Guardar gasto':
        monto= values["MONTO"]
        categoria= values["CATEGORIA"]
        fecha= values["FECHA"]
        guardar_gastos(ventana, fecha, monto, categoria)

ventana.close()