import FreeSimpleGUI as sg
import csv
from pec.funciones import meta_ahorro, num_semanas, aporte_actual, progreso

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar reporte"), sg.Button("Ver progreso")]
]

window = sg.Window("Reto de ahorro personalizado", layout, font=("Arial", 20))

while True:
    evento, valores = window.read()

    if evento == sg.WIN_CLOSED:
        break

    elif evento == "Registrar reporte":
        try:
            meta = meta_ahorro(valores["META"])
            semanas = num_semanas(valores["SEMANAS"])
            aporte = aporte_actual(valores["APORTE"])

            with open('datos.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([meta, semanas, aporte])

            sg.popup("Datos registrados correctamente")

        except ValueError:
            sg.popup("Error", "Por favor, ingresa datos válidos.")

    elif evento == "Ver progreso":
        try:
            with open('datos.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                datos = list(reader)

                meta = meta_ahorro(datos[-1][0])
                semanas = num_semanas(datos[-1][1])
                aporte = aporte_actual(datos[-1][2])

                porcentaje = progreso(aporte, meta)

                mensaje = (
                    "Estás haciendo un buen progreso." if porcentaje >= 100
                    else "Debes aumentar tus aportes para alcanzar tu meta."
                )

                layout_progreso = [
                    [sg.Text(f"Meta de ahorro: {meta}")],
                    [sg.Text(f"Número de semanas: {semanas}")],
                    [sg.Text(f"Aporte actual: {aporte}")],
                    [sg.Text(f"Progreso: {porcentaje:.2f}%")],
                    [sg.Text(mensaje)],
                    [sg.Button("Cerrar")]
                ]

                window_progreso = sg.Window("Avances de ahorro", layout_progreso, font=("Arial", 20))
                while True:
                    ev, _ = window_progreso.read()
                    if ev == "Cerrar" or ev == sg.WIN_CLOSED:
                        break
                window_progreso.close()

        except:
            sg.popup("Error", "Registra tus datos antes de ver tu progreso.")

window.close()