import csv
import os
from funciones import *
import FreeSimpleGUI as sg

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="meta")],
    [sg.Text("Número de semanas:"), sg.Input(key="semanas")],
    [sg.Text("Aporte semanal:"), sg.Input(key="aporte")],
    [sg.Text("Semanas transcurridas: "), sg.Input(key="sem_trans")],
    [sg.Button("Ver progreso"), sg.Button("Salir"),sg.Button("Registrar aporte")],
    [sg.Multiline(size=(50, 6), key="salida",disabled=True)],
]
ventana = sg.Window("Meta de ahorro", layout)

while True:
    event, values = ventana.read()
    if event == "Ver progreso":

        try:
            meta = float(values["meta"])
            semanas = int(values["semanas"])
            aporte = float(values["aporte"])
            sem_trans = int(values["sem_trans"])
            resultado = clacular_progreso(meta, semanas, aporte, sem_trans)
            ventana["salida"].update(resultado)
        except ValueError:
            ventana["salida"].update("Por favor, ingresa solo números válidos.")

    if event == "Registrar aporte":
        aporte = int(values["aporte"])
        guardar_csv(aporte)

    elif event == sg.WIN_CLOSED or event == "Salir":
        break

ventana.close()