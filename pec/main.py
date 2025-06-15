import FreeSimpleGUI as sg
from funciones import guardar_aporte, calcular_progreso

sg.theme("DarkBlue")

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("Reto de Ahorro", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Registrar aporte":
        meta, semanas, aporte = values["META"], values["SEMANAS"], values["APORTE"]
        if meta and semanas and aporte:
            guardar_aporte(meta, semanas, aporte)
            sg.popup("¡Aporte registrado!", title="Éxito")
        else:
            sg.popup("Completa todos los campos", title="Error")

    if event == "Ver progreso":
        meta, semanas = values["META"], values["SEMANAS"]
        if meta and semanas:
            ahorrado, faltante, porcentaje, estado = calcular_progreso(meta, semanas)
            sg.popup(f"Has ahorrado ${ahorrado} ({porcentaje}%)\nTe faltan ${faltante} para tu meta.\nEstado: {estado}", title="Progreso")
        else:
            sg.popup("Ingresa la meta y semanas para ver el progreso", title="Error")

window.close()
