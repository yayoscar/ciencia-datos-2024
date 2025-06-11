import FreeSimpleGUI as sg
from funciones import obtener_tasa, calcular_ahorro, guardar_resultado_csv
sg.theme("DrakPurple6")
fuente=("Helvetica", 12)

layout = [
    [sg.Text("Monto inicial:"), sg.Input(key="inicial")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="mensual")],
    [sg.Text("Meses:"), sg.Input(key="meses")],
    [sg.Text("Banco:"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="banco")],
    [sg.Button("Calcular")]
]

ventana = sg.Window("Simulador de ahorro", layout)

while True:
    evento, valores = ventana.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "Calcular":
        try:
            inicial = float(valores["inicial"])
            mensual = float(valores["mensual"])
            meses = int(valores["meses"])
            banco = valores["banco"]

            tasa = obtener_tasa(banco)
            total = calcular_ahorro(inicial, mensual, meses, tasa)

            sg.popup(f"Tendrías ${total} al finalizar los {meses} meses.")

            guardar_resultado_csv("pec/datos.csv", inicial, mensual, meses, banco, total)

        except Exception as e:
            sg.popup("Error:", str(e), title="Error", font=("Helvetica",11))

ventana.close()