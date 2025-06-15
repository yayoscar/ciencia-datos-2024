import FreeSimpleGUI as sg
from datetime import datetime
from funciones import calcular_ahorro, guardar_csv, tasass

layout = [
    [sg.Text("Monto inicial:"), sg.Input(key="INICIAL")],
    [sg.Text("Ahorro mensual:"), sg.Input(key="MENSUAL")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Text("Banco:"), sg.Combo(list(tasass.keys()), key="BANCO")],
    [sg.Button("Calcular"), sg.Button("Salir")]
]

ventana = sg.Window("Simulador de Ahorro", layout)

while True:
    evento, valores = ventana.read()
    if evento in (sg.WIN_CLOSED, "Salir"):
        break

    try:
        inicial = float(valores["INICIAL"])
        mensual = float(valores["MENSUAL"])
        meses = int(valores["MESES"])
        banco = valores["BANCO"]

        if banco not in tasass:
            sg.popup("Error", "Selecciona un banco válido.")
            continue

        tasa = tasass[banco]
        total = calcular_ahorro(inicial, mensual, meses, tasa)

        mensaje = f"Tendrías ${total:,.2f} al finalizar {meses} meses en {banco}."
        sg.popup("Resultado", mensaje)

        guardar_csv(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    banco, inicial, mensual, meses, tasa, total)

    except ValueError:
        sg.popup("Error", "Ingresa valores numéricos válidos.")

ventana.close()
