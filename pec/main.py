import FreeSimpleGUI as sg

layout = [
    [sg.Text("Registro de Gastos: ", pad=(60,20), font=("Cascadia Mono", 40))],
    [sg.Text("Monto de gasto: "), sg.Input(key= "monto", size=(20, 20))],
    [sg.Text("Categoría: "), sg.Combo(["Comida","Transporte","Salud","Ropa o accesorios","Impuestos","Otro"], key = "categoría")],
    [sg.Text("Nombre del gasto (Opcional): "), sg.Input(key= "nombre", size=(20, 90))],
    [sg.Text("Fecha (Opcional): "), sg.Input(key= "fecha", size=(20, 90))],
    [sg.Canvas(size=(320, 20), background_color='black'), sg.Text("DD/MM/AAAA")],
    [sg.Button("Guardar"), sg.Button("Ver resumen"), sg.Button("Salir")]
]
ventana = sg.Window("Registro de Gastos y Categorías", layout, font= ("Cascadia Mono", 15))

while True:
    evento, valor = ventana.read()
    if evento == sg.WIN_CLOSED or evento == "Salir":
        break
    if evento == "Guardar":
        continue
ventana.close()
