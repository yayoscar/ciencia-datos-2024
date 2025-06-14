import FreeSimpleGUI as sg
import os
from funciones import guardar_datos_en_archivo
from funciones import calcular_progreso
from funciones import reiniciar_meta

layout = [
[sg.Text("Meta de ahorro:"), sg.Input(key="META")],
[sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
[sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
[sg.Text("Ejemplo de aporte: 200,300,600,500,400")],
[sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Reiniciar metas")]
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
            sg.popup("Aporte registrado con exito :)")
        except ValueError:
            sg.popup("Porfavor ingrese datos validos")

    elif evento == "Ver progreso":
        mensaje = calcular_progreso()
        sg.popup(mensaje)

    elif evento == "Reiniciar metas":
        reiniciar_meta()
        sg.popup("Meta reiniciada Ya puedes crear una nueva")

window.close()