import FreeSimpleGUI as sg
import funciones as func


layout = [
    [sg.Text("Registro de Gastos: ", pad=(60,20), font=("Cascadia Mono", 40))],
    [sg.Text("Monto de gasto: "),sg.Push(), sg.Input(key= "monto", size=(20, 20))],
    [sg.Text("Categoría: "),sg.Push(), sg.Combo(["Comida","Transporte","Salud","Ropa o accesorios","Impuestos","Vivienda","Otro"], key = "categoria", size=(19,19))],
    [sg.Text("Fecha (Opcional): "),sg.Push(), sg.Input(key= "fecha", size=(20, 90))],
    [sg.Push(), sg.Text("DD/MM/AAAA")],
    [sg.Image(sg.EMOJI_BASE64_COOL),sg.Push(), sg.Button("Guardar"), sg.Button("Ver registro"), sg.Button("Ver resumen"), sg.Button("Salir")]
]
ventana = sg.Window("Registro de Gastos y Categorías", layout, font= ("Cascadia Mono", 15), icon=(sg.EMOJI_BASE64_JASON))

while True:
    evento, valor = ventana.read()
    if evento == sg.WIN_CLOSED or evento == "Salir":
        break
    elif evento == "Guardar":
        fila = func.prepara_datos(valor)
        if func.comprobar(fila):
            func.añade_csv(fila)
            sg.popup_timed("¡Guardado con éxito!", auto_close_duration= 1)
        else:
            continue
    elif evento == "Ver registro":
        func.mostrar_tabla()
        continue
    elif evento == "Ver resumen":
        func.mostrar_resumen()
        continue

ventana.close()
