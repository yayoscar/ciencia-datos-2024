import FreeSimpleGUI as sg
from numpy.ma.core import append

from funciones import guardar_gasto, obtener_resumen

nombre_archivo = "datos.csv"
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
                guardar_gasto(nombre_archivo, monto, categoria, fecha)
                sg.popup("Gasto guardado correctamente.")
                nuevo = f"Gasto Guardado: ${monto} - {categoria} - {fecha}\n"
                ventana["SALIDA"].update(nuevo, append=True)
                ventana["MONTO"].update("")
                ventana["FECHA"].update("")
                ventana["CATEGORIA"].update("")
            except ValueError:
                sg.popup_error("El monto debe ser un número válido.")
        else:
            sg.popup_error("Debe completar el monto y la categoría.")

    elif evento == "Ver resumen":
        resumen, total = obtener_resumen(nombre_archivo)
        salida = ""
        for cat, suma in resumen.items():
            salida += f"{cat}: ${suma:.2f}\n"
        salida += f"\nTotal: ${total:.2f}"
        ventana["SALIDA"].update(salida)

ventana.close()