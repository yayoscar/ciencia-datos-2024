import FreeSimpleGUI as sg
from funciones import guardar_gasto, obtener_resumen

sg.theme("DarkRed")

layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
    [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen"), sg.Exit()],
    [sg.Multiline(size=(40, 10), key="SALIDA", disabled=True)]
]

ventana = sg.Window("Registro de Gastos y Categorías", layout, font=("Bell MT", 15))

while True:
    evento, valores = ventana.read()
    if evento in (sg.WINDOW_CLOSED, "Exit"):
        break

    if evento == "Guardar gasto":
        monto = valores["MONTO"]
        categoria = valores["CATEGORIA"]
        fecha = valores["FECHA"]

        if monto and categoria:
            try:
                monto = float(monto)
                guardar_gasto(monto, categoria, fecha)
                ventana["SALIDA"].update("Gasto guardado\n", append=True)
            except ValueError:
                ventana["SALIDA"].update("Monto inválido\n", append=True)
        else:
            ventana["SALIDA"].update("Faltan datos obligatorios\n", append=True)

    elif evento == "Ver resumen":
        resumen, total = obtener_resumen()
        salida = ""
        for cat, suma in resumen.items():
            salida += f"{cat}: ${suma:.2f}\n"
        salida += f"\nTotal: ${total:.2f}"
        ventana["SALIDA"].update(salida)

ventana.close()