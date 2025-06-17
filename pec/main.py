import FreeSimpleGUI as sg
layout = [
[sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
[sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"],
key="CATEGORIA")],
[sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
[sg.Button("Guardar gasto"), sg.Button("Ver resumen")]

]
ventana = sg.Window('Registros de gastos y categorias', layout)
gastos = []
while True:
    event, values = ventana.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Guardar gasto":
        monto = values["MONTO"]
        categoria = values["CATEGORIA"]
        fecha = values["FECHA"]
        if not monto or not categoria:
            sg.popup("Porfis, completa al menos el monto y la categora.")
        else:
            try:
                monto = float(monto)
                gastos.append({
                    "monto": monto,
                    "categoria": categoria,
                    "fecha": fecha


                })
                sg.popup("Gasto guardado.")
            except ValueError:
                sg.popup("El monto debe ser un numero no una palabra")
    elif event == "Ver resumen":
        if not gastos:
            sg.popup("No hay gastos que se hayan registrados")
            continue

        resumen = {}
        for gasto in gastos:
            quepongoxd = gasto["categoria"]
            resumen[quepongoxd] = resumen.get(quepongoxd, 0) + gasto["monto"]

        mensaje = "Resuemn de gastos por catergoria:"
        for categoria, total in resumen.items():
            mensaje += f"{categoria}: ${total:.2f}\n"

        sg.popup("Resmen", mensaje)

ventana.close()