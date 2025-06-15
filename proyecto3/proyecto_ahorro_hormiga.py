import FreeSimpleGUI as sg

layout =[
[sg.Text("Nombre del gasto hormiga a eliminar:"), sg.Input(key="NOMBRE_GASTOS")],
[sg.Text("El precio por unidad:"), sg.Input(key="EL_PRECIO_POR_UNIDAD")],
[sg.Text("Veces por semana:"), sg.Input(key="VECES_SEMANA")],
[sg.Text("Meses:"), sg.Input(key="CANTIDAD_MESES")],
[sg.Button("Calcular ahorro")],
[sg.Button("Salir")]
]

window = sg.Window("Ahorrador de gastos hormiga. ",layout,font=("Century",25))

while True:
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED or evento == "Salir":
        break
    if evento == "Calcular ahorro":
        try:
            texto_gastos = valores["NOMBRE_GASTOS"]
            precio_unidad = float(valores["EL_PRECIO_POR_UNIDAD"])
            veces_semana = int(valores["VECES_SEMANA"])
            meses_semana = int(valores["CANTIDAD_MESES"])

            ahorro = precio_unidad * veces_semana * 4.33 * meses_semana
            mensaje = f"Con ese gasto, gastas {ahorro:.2f} en tan solo {meses_semana} meses, si dejaras de consumir '{texto_gastos}' a ${precio_unidad} por unidad, {veces_semana} veces por semana durante {meses_semana} meses, ahorrarías aporximadamente ${ahorro:.2f}."
        except ValueError:
            mensaje = "Por favor, asegúrate de ingresar solo números válidos en los campos numéricos."

            sg.popup(mensaje, title="Resultado")
window.close()
