import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿A qué temperatura se encuentra tu ciudad? (°C)")],
    [sg.Slider(range=(0, 100), orientation="h", key="SLIDER")],
    [sg.Button("Mostrar")]
]

window = sg.Window("Temperatura", layout, font=("Arial", 20))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Mostrar":
        sg.popup("Temperatura",
                 f"La temperatura seleccionada es: {values['SLIDER']}°C")

window.close()