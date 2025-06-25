import FreeSimpleGUI as sg
import os
from funciones import guardar_datos_en_archivo,calcular_progreso,reiniciar_meta

layout = [
[sg.Text("Meta de ahorro:",size=(18,1),text_color="white", background_color="green"), sg.Input(key="META"), ],
[sg.Text("Número de semanas:",size=(18,1),text_color="white", background_color="green"), sg.Input(key="SEMANAS")],
[sg.Text("Aporte actual:",size=(18,1),text_color="white", background_color="green"), sg.Input(key="APORTE")],
[sg.Text("Ejemplo de aporte: 200,300,600,500,400",text_color="white", background_color="green")],
[sg.Button("Registrar aporte",size=(15,1)),
 sg.Button("Ver progreso",size=(15,1)),
 sg.Button("Reiniciar metas",size=(15,1))]
]

ruta_icono = "Aigis-icon.ico"
if not os.path.exists(ruta_icono):
    ruta_icono = None

window = sg.Window("Reto de Ahorro", layout, background_color="Green",icon=ruta_icono)


while True:
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED:
        break
    elif evento == "Registrar aporte":
        try:
            meta_usuario = float(valores["META"])
            semanas_usuario = int(valores["SEMANAS"])
            aporte_usuario = valores["APORTE"].split(",")
            for aporte in aporte_usuario:
                aporte = aporte.strip()
                if aporte:
                    guardar_datos_en_archivo(meta_usuario,semanas_usuario,float(aporte))
            sg.popup("Aporte registrado con exito :)", auto_close_duration=2)
        except ValueError:
            sg.popup("Porfavor Ingrese Datos Validos")

    elif evento == "Ver progreso":
        mensaje = calcular_progreso()
        sg.popup(mensaje)

    elif evento == "Reiniciar metas":
        reiniciar_meta()
        sg.popup("Meta reiniciada Ya puedes crear una nueva")

window.close()