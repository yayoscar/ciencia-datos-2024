import FreeSimpleGUI as sg
from funciones import guardar_gasto,ver_resumen
layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
    [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen")],
    [sg.Multiline("", size=(30, 10), key="RESUMEN", disabled=True)]
]
ventana =  sg.Window(" Registro de Gastos y Categorías",layout,font=('Britannic Negrita',20))
while True:
    evento, values = ventana.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == "Guardar gasto":
        monto = values["MONTO"]
        categoria = values["CATEGORIA"]
        fecha = values["FECHA"]
        guardar_gasto(monto, categoria, fecha)
    elif evento == "Ver resumen":
        resumen = ver_resumen()
        ventana['RESUMEN'].update(resumen)
        ventana.read()
ventana.close()

