import FreeSimpleGUI as sg

layout = [
    [sg.Text("Selecciona la temperatura (°C):")],
    [sg.Slider(range=(0, 100), orientation="h", key="TEMP")],
    [sg.Button("Mostrar")]
]

window = sg.Window("Control de Temperatura", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Mostrar":
        temp = values["TEMP"]
        if temp < 20:
            mensaje = "Frío"
        elif 20 <= temp <= 30:
            mensaje = "Agradable"
        else:
            mensaje = "Caliente"
        sg.popup(f"Temperatura: {int(temp)}°C\nEstado: {mensaje}")

window.close()