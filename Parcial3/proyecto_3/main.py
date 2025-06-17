import FreeSimpleGUI as sg
from funciones import calcular_ahorro
from guardar_csv import guardar_resultado

layout = [
[sg.Text("Nombre del gasto hormiga que quiera eliminar:"), sg.Input(key="NOMBRE_GASTOOS")],
[sg.Text("Precio por unidad:"), sg.Input(key="PRECIO_UNIDAD")],
[sg.Text("Las veces por semana:"), sg.Input(key="VECES")],
[sg.Text("Meses:"), sg.Input(key="MESES")],
[sg.Button("Calcular ahorro")],
[sg.Button("Salir")]
]

window = sg.Window("Calculadora de ahorro de gastos hormiga. ",layout,font=("Century",25))

while True:
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED or evento == "Salir":
        break
    if evento == "Calcular ahorro":
        nombre_gasto = valores["NOMBRE_GASTOOS"]
        precio_unidad = valores["PRECIO_UNIDAD"]
        veces_por_semana = valores["VECES"]
        meses = valores["MESES"]

        mensaje = calcular_ahorro(nombre_gasto, precio_unidad, veces_por_semana, meses)
        sg.popup(mensaje, title="Resultado")

        try:
            precio = float(precio_unidad)
            veces = int(veces_por_semana)
            meses = int(meses)
            ahorro = precio * veces * 4.33 * meses  # Recalcular ahorro para guardar en CSV
            guardar_resultado(nombre_gasto, precio_unidad, veces_por_semana, meses, ahorro)
        except ValueError:
            sg.popup("No se pudo guardar en el CSV: Valores numéricos inválidos.", title="Error")

window.close()
