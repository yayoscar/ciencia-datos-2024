import FreeSimpleGUI as sg
from funciones import guardar_gasto, generar_resumen

layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
    [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen")]
]

window = sg.Window("Registro de Gastos", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Guardar gasto":
        try:
            monto = float(values["MONTO"])
            categoria = values["CATEGORIA"]
            fecha = values["FECHA"]
            guardar_gasto(monto, categoria, fecha)
            sg.popup("Gasto guardado exitosamente.")
        except ValueError:
            sg.popup_error("Ingresa un monto válido.")

    elif event == "Ver resumen":
        resumen, total = generar_resumen()
        if resumen:
            mensaje = "\n".join([f"{cat}: ${resumen[cat]:.2f}" for cat in resumen])
            mensaje += f"\n\nTotal: ${total:.2f}"
            sg.popup("Resumen de gastos", mensaje)
        else:
            sg.popup("No hay gastos registrados.")

window.close()