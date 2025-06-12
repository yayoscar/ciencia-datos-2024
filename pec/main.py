import FreeSimpleGUI as sg


layout=[
    [sg.Text("Nombre del gasto hormiga (ej.Cafe):",size=(20, 1)), sg.Input(key="NOMBRE")],
    [sg.Text("Precio por unidad",size=(20, 1)), sg.Input(key="PRECIO")],
    [sg.Text("Veces por semana:",size=(20,1)), sg.Input(key="VECES")],
    [sg.Text("Meses:",size=(20, 1)), sg.Input(key="VECES")],
    [sg.Button("Calcular ahorro"), sg.Button("Salir")],
    [sg.Text(size=(40, 2), key="RESULTADO")]

]

ventana = sg.Window("Proyecto 3: Calcular ahorro",layout,font=("Arial", 20))
while True:
   evento, valores = Window.read()
    if evento ==sg.WIN_CLOSED or evento == "Salir":
        break

    if evento == "Calcular ahorro":
        try:
            nombre = valores["GASTO HORMIGA"]
            precio = valores["PRECIO POR UNI"]
            veces= valores["VECES POR SEMANA"]
            meses = valores["MESES"]

            gasto_total = precio * veces * 4 * meses
            ventana["RESULTADO"]




Window.close()