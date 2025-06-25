import FreeSimpleGUI as sg
import csv
import os

ARCHIVO_CSV = "aportes.csv"

# Crear archivo si no existe, con encabezado
if not os.path.exists(ARCHIVO_CSV):
    with open(ARCHIVO_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Aporte"])  # Encabezado

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("PROYECTO_PEC", layout, font=("Arial", 20))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Registrar aporte":
        try:
            aporte = float(values["APORTE"])

            # Guardar el aporte en el archivo CSV
            with open(ARCHIVO_CSV, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([aporte])

            sg.popup("Aporte registrado correctamente.", title="Éxito")

        except ValueError:
            sg.popup("Por favor, ingresa un número válido para el aporte.", title="Error")

    elif event == "Ver progreso":
        try:
            meta = float(values["META"])
            total_aportado = 0.0

            # Leer todos los aportes del archivo CSV
            with open(ARCHIVO_CSV, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar encabezado
                for row in reader:
                    if row and row[0].strip():
                        total_aportado += float(row[0])

            restante = meta - total_aportado

            sg.popup(f"Total aportado: ${total_aportado:.2f}\n"
                     f"Meta de ahorro: ${meta:.2f}\n"
                     f"Restante para la meta: ${restante:.2f}", title="Progreso de ahorro")

        except ValueError:
            sg.popup("Por favor, asegúrate de que la meta sea un número válido.", title="Error")

window.close()
