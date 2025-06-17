import FreeSimpleGUI as sg
from funciones import *
layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
    [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen"),sg.Button("Ver gastos")],
    [sg.Multiline("", size=(20, 10), key="RESUMEN", disabled=True)]
]

ventana = sg.Window("Registro de Gastos y Categorías", layout, font=('Britannic Negrita', 16))

while True:
    evento, values = ventana.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == "Guardar gasto":
        monto = values["MONTO"]
        categoria = values["CATEGORIA"]
        fecha = values["FECHA"]

        if fecha.strip() == "":
            fecha = obtener_fecha()

        mensaje = guardar_gasto(monto, categoria, fecha)
        ventana['RESUMEN'].update(mensaje)

    elif evento == "Ver resumen":
        resumen = mostrar_resumen()
        ventana['RESUMEN'].update(resumen)
    elif evento == "Ver gastos":
        gastos = mostrar_gastos()
        ventana['RESUMEN'].update(gastos)


ventana.close()

