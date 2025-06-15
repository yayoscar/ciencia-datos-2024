import FreeSimpleGUI as sg
import csv

tasas_anuales = {
    "Hey Banco": 10.5,
    "NU": 13.5,
    "Finsus": 15.0
}

def calcular_monto_final(inicial, mensual, meses, tasa_anual):
    tasa_mensual = tasa_anual / 100 / 12
    monto = inicial
    for _ in range(meses):
        monto += mensual
        monto += monto * tasa_mensual
    return round(monto, 2)


layout = [
    [sg.Text("Monto inicial:"), sg.Input(key="INICIAL")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="MENSUAL")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Text("Banco:"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="BANCO")],
    [sg.Button("Calcular")]
]

window = sg.Window("Calculadora de Interés Compuesto", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Calcular":
        try:
            inicial = float(values["INICIAL"])
            mensual = float(values["MENSUAL"])
            meses = int(values["MESES"])
            banco = values["BANCO"]

            if banco not in tasas_anuales:
                sg.popup("Selecciona un banco válido.")
                continue

            tasa = tasas_anuales[banco]
            monto_final = calcular_monto_final(inicial, mensual, meses, tasa)

            sg.popup(f"Tendrás ${monto_final} al finalizar los {meses} meses.")


            with open("resultado_inversion.csv", "a", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([inicial, mensual, meses, banco, tasa, monto_final])

        except ValueError:
            sg.popup("Por favor, ingresa solo números válidos.")

window.close()