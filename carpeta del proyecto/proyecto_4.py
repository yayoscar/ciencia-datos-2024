import FreeSimpleGUI as sg

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("PROYECTO_PEC", layout, font=("Arial", 20))

# Lista para almacenar los aportes
aportes = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Registrar aporte":
        try:
            aporte = float(values["APORTE"])
            aportes.append(aporte)
            sg.popup("Aporte registrado correctamente.", title="Éxito")
        except ValueError:
            sg.popup("Por favor, ingresa un número válido para el aporte.", title="Error")

    elif event == "Ver progreso":
        try:
            meta = float(values["META"])
            total_aportado = sum(aportes)
            restante = meta - total_aportado
            sg.popup(f"Total aportado: ${total_aportado:.2f}\n"
                     f"Meta de ahorro: ${meta:.2f}\n"
                     f"Restante para la meta: ${restante:.2f}", title="Progreso de ahorro")
        except ValueError:
            sg.popup("Por favor, asegúrate de que la meta sea un número válido.", title="Error")

window.close()
