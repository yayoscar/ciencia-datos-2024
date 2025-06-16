import FreeSimpleGUI as sg
import csv
from funciones import obtener_tasa, calcular_monto_final

sg.theme("Blue")

layout = [
    [sg.Text("Monto inicial:"), sg.Input(key="INICIAL")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="MENSUAL")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Text("Banco:"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="BANCO")],
    [sg.Button("Calcular"), sg.Button("Salir")]
]

window = sg.Window("Simulador de Ahorro", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Salir"):
        break
    if event == "Calcular":
        try:
            monto_inicial = float(values["INICIAL"])
            ahorro_mensual = float(values["MENSUAL"])
            meses = int(values["MESES"])
            banco = values["BANCO"]

            tasa = obtener_tasa(banco)
            resultado = calcular_monto_final(monto_inicial, ahorro_mensual, meses, tasa)

            sg.popup(f"Monto final después de {meses} meses: ${resultado}")

            with open("pec/datos.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([monto_inicial, ahorro_mensual, meses, banco, resultado])

        except ValueError:
            sg.popup("Por favor ingresa valores numéricos válidos.")

window.close()



