import FreeSimpleGUI as sg

import funciones as func


layout = [
    [sg.Text("Registro de Gastos: ", pad=(60,20), font=("Cascadia Mono", 40))],
    [sg.Text("Monto de gasto: "),sg.Push(background_color='yellow'), sg.Input(key= "monto", size=(20, 20))],
    [sg.Text("Categoría: "),sg.Push(background_color='yellow'), sg.Combo(["Comida","Transporte","Salud","Ropa o accesorios","Impuestos","Vivienda","Otro"], key = "categoria", size=(19,19))],
    [sg.Text("Fecha (Opcional): "),sg.Push(background_color='yellow'), sg.Input(key= "fecha", size=(20, 90))],
    [sg.Push(background_color='yellow'), sg.Text("DD/MM/AAAA")],
    [sg.Image(sg.EMOJI_BASE64_FINGERS_CROSSED),sg.Push(background_color='yellow'), sg.Button("Guardar"), sg.Button("Ver resumen"), sg.Button("Salir")]
]
ventana = sg.Window("Registro de Gastos y Categorías", layout, font= ("Cascadia Mono", 15), icon=(sg.EMOJI_BASE64_HAPPY_THUMBS_UP))

while True:
    evento, valor = ventana.read()
    if evento == sg.WIN_CLOSED or evento == "Salir":
        break
    elif evento == "Guardar":
        fila = func.prepara_datos(valor)
        if func.es_numerico(fila):
            func.añade_csv(fila)
        else:
            continue
        break
    elif evento == "Ver resumen":
        lector = func.leer_dict()


ventana.close()
