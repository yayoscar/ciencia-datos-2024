import FreeSimpleGUI as sg
import funciones as func
from pec.funciones import borrar_campos

layout = [
    [sg.Text("Registro de Gastos: ", pad=(60,20), font=("Cascadia Mono", 40), background_color="#ECAD83", text_color="#BA4329")],
    [sg.Text("Monto de gasto: ", background_color="#ECAD83", text_color="#611227"),sg.Push(background_color="#ECAD83"), sg.Input(key= "monto", size=(20, 20), text_color="#611227")],
    [sg.Text("Categoría: ", background_color="#ECAD83", text_color="#611227"),sg.Push(background_color="#ECAD83"), sg.Combo(["Comida","Transporte","Salud","Ropa o accesorios","Impuestos","Vivienda","Otro"], key = "categoria", size=(19,19), button_background_color="#8F1535")],
    [sg.Text("Fecha (Opcional): ", background_color="#ECAD83", text_color="#611227"),sg.Push(background_color="#ECAD83"), sg.Input(key= "fecha", size=(20, 90), text_color="#611227")],
    [sg.Push(background_color="#ECAD83"), sg.Text("DD/MM/AAAA", background_color="#ECAD83", text_color="#611227")],
    [sg.Image(sg.EMOJI_BASE64_HEAD_EXPLODE, background_color="#ECAD83"),sg.Push(background_color="#ECAD83"), sg.Button("Guardar", button_color="#8F1535"), sg.Button("Ver registro", button_color="#8F1535"), sg.Button("Ver resumen", button_color="#8F1535"), sg.Button("Salir", button_color="#8F1535")]
]
ventana = sg.Window("Registro de Gastos y Categorías", layout, font= ("Cascadia Mono", 15), icon=(sg.EMOJI_BASE64_JASON), background_color="#ECAD83")

while True:
    evento, valor = ventana.read()
    if evento == sg.WIN_CLOSED or evento == "Salir":
        sg.popup("Hecho por Yana, páseme con 10", font=("Cascadia Mono", 50), background_color="black", text_color="White", button_color="Yellow")
        break
    elif evento == "Guardar":
        fila = func.prepara_datos(valor)
        si = func.comprobar(fila)
        if si:
            func.añade_csv(fila)
            sg.popup_timed("¡Guardado con éxito!", auto_close_duration=.6, background_color="#611227", font=("Cascadia Mono", 16), button_color="#EA9CB1")
            borrar_campos(ventana)
        else:
            continue
    elif evento == "Ver registro":
        func.mostrar_tabla()
        continue
    elif evento == "Ver resumen":
        func.mostrar_resumen()
        continue

ventana.close()
