import FreeSimpleGUI as sg
import csv
layout = [
 [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
 [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"],
key="CATEGORIA")],
 [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
 [sg.Button("Guardar gasto"), sg.Button("Ver resumen")]
 ]
window = sg.Window("Registro de Gastos y Categorías",layout,font=('Arial',25))
window.read()

datos = [
    ["MONTO"],
    ["CATEGORIA"],
    ['FECHA']

]


with open("datos.csv","w") as archivo:
          writer = csv.writer(archivo)
          writer.writerows(datos)

