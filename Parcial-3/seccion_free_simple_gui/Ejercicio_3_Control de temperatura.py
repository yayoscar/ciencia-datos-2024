import FreeSimpleGUI as sg

layout = [
    [sg.Text("Temperatura (°C):"), sg.Slider(range=(0, 100), orientation='h', key="TEMP")],
    [sg.Button("Mostrar Temperatura")]
]

window = sg.Window("Control de Temperatura", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,):
        break
    elif event == "Mostrar Temperatura":
        sg.popup(f"Temperatura seleccionada: {values['TEMP']} °C")

window.close()
