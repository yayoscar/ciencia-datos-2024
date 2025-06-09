import FreeSimpleGUI as sg

import funciones as func

layout = [
    [sg.Text("Registro de Gastos: ", pad=(60,20), font=("Cascadia Mono", 40))],
    [sg.Text("Monto de gasto: "), sg.Input(key= "monto", size=(20, 20))],
    [sg.Text("Categoría: "), sg.Combo(["Comida","Transporte","Salud","Ropa o accesorios","Impuestos","Vivienda","Otro"], key = "categoria")],
    [sg.Text("Fecha (Opcional): "), sg.Input(key= "fecha", size=(20, 90))],
    [sg.Canvas(size=(340, 20), background_color='black'), sg.Text("DD/MM/AAAA")],
    [sg.Button("Guardar"), sg.Button("Ver resumen"), sg.Button("Salir")]
]
ventana = sg.Window("Registro de Gastos y Categorías", layout, font= ("Cascadia Mono", 15))

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
        continue

ventana.close()
