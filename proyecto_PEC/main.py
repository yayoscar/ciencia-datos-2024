import FreeSimpleGUI as sg
from funciones import cargar_datos, guardar_datos, calcular_progreso

datos = cargar_datos()
meta = datos["meta"]
semanas = datos["semanas"]
aportes = datos["aportes"]

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(default_text=str(meta), key="META")],
    [sg.Text("Número de semanas:"), sg.Input(default_text=str(semanas), key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Salir")]
]

window = sg.Window("Reto de Ahorro Personalizado", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Registrar aporte":
        try:

            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            aporte = float(values["APORTE"])
            aportes.append(aporte)
            guardar_datos(meta, semanas, aportes)
            sg.popup(" Aporte registrado con éxito.")
        except ValueError:
            sg.popup(" Verifica que todos los campos tengan valores válidos.")

    if event == "Ver progreso":
        total, porcentaje, falta = calcular_progreso(meta, aportes)
        mensaje = f"Has ahorrado ${total:.2f} ({porcentaje:.1f}%)\n"
        if total >= meta:
            mensaje += " ¡Meta cumplida!"
        else:
            mensaje += f"Te faltan ${falta:.2f} para alcanzar tu meta."
        sg.popup("Progreso de Ahorro", mensaje)

window.close()