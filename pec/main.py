import FreeSimpleGUI as sg
from funciones import obtener_tasa, calcular_ahorro, guardar_resultado_csv

layout = [
    [sg.Text("cantidad inicial:"), sg.Input(key="incial")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="mensual")],
    [sg.Text("Meses:"), sg.Input(key="meses")],
    [sg.Text("Banco:"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="banco")],
    [sg.Button("Calcular")]
]

ventana = sg.Window("simulador de ahorro", layout)

while True:
    evento, valores = ventana.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "calcular":
        try:
            monto_inicial = float(valores["incial"])
            mensual = float(valores["mensual"])
            meses = int(valores["meses"])
            banco = valores["banco"]

            tasa = obtener_tasa(banco)
            total = calcular_ahorro(monto_inicial, mensual, meses, tasa)

            sg.popup(f"Tendrías ${total} al finalizar los {meses} meses.")

            guardar_resultado_csv("datos.csv", monto_inicial, mensual, meses, banco, total)

        except Exception as e:
            sg.popup("Error: Verifica que los datos sean correctos.")

ventana.close()