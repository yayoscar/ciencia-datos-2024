import FreeSimpleGUI as sg

layout = [
    [sg.Text("Temperatura:"), sg.Slider(range=(0, 100), orientation="h", key="TEMP")],
    [sg.Button("Evaluar")]
]

window = sg.Window("Temperatura", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Evaluar":
        temp = values["TEMP"]
        if temp < 20:
            sg.popup("Frío")
        elif 20 <= temp <= 30:
            sg.popup("Agradable")
        else:
            sg.popup("Caliente")

window.close()
