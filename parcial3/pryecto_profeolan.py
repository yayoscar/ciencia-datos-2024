import FreeSimpleGUI as sg
import csv

# Diccionario con tasas anuales (ejemplo)
tasas = {
    "Hey Banco": 0.10,    # 10% anual
    "NU": 0.135,          # 13.5% anual
    "Finsus": 0.145       # 14.5% anual
}

# Layout de la ventana
layout = [
    [sg.Text("Monto inicial:"), sg.Input(key="INICIAL")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="MENSUAL")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Text("Banco:"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="BANCO")],
    [sg.Button("Calcular")]
]

# Crear ventana
ventana = sg.Window("Simulador de Ahorro", layout)

# Función para calcular interés compuesto
def calcular_ahorro(monto_inicial, mensual, meses, tasa_anual):
    tasa_mensual = tasa_anual / 12
    total = monto_inicial
    for _ in range(meses):
        total = (total + mensual) * (1 + tasa_mensual)
    return round(total, 2)

# Loop principal
while True:
    evento, valores = ventana.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "Calcular":
        try:
            inicial = float(valores["INICIAL"])
            mensual = float(valores["MENSUAL"])
            meses = int(valores["MESES"])
            banco = valores["BANCO"]

            tasa = tasas.get(banco, 0)
            total = calcular_ahorro(inicial, mensual, meses, tasa)

            sg.popup(f"Tendrías ${total} al finalizar los {meses} meses.")

            # Guardar en CSV
            with open("resultado_ahorro.csv", "w", newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["Monto Inicial", "Mensual", "Meses", "Banco", "Total Final"])
                writer.writerow([inicial, mensual, meses, banco, total])

        except ValueError:
            sg.popup("Por favor, ingresa números válidos.")

ventana.close()