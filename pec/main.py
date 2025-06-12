import FreeSimpleGUI as sg
import csv
from pec.funciones import mostrar_gastos, guardar_datos

layout = [
 [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
 [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"],
key="CATEGORIA")],
 [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
 [sg.Button("Guardar gasto"), sg.Button("Ver resumen")]
 ]

ventana = sg.Window("Registro de Gastos y Categoría",layout,font=("Arial",20),)


while True:
    evento, values = ventana.read()
    if evento == "Guardar gasto":
        monto = values["MONTO"]
        categoria = values["CATEGORIA"]
        fecha = values["FECHA"]
        if not monto or not categoria:
            sg.popup("Por favor, completa al menos el monto y la categoría.")
        else:
            guardar_datos(monto, categoria, fecha)
            sg.popup("Datos guardados")
    elif evento == "Ver resumen":
        sg.popup(mostrar_gastos())
    elif evento == sg.WIN_CLOSED:
        break
ventana.close()