import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Verificar")]
]

window = sg.Window("Verificar Edad", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Verificar":
        nombre = values["NOMBRE"]
        try:
            edad = int(values["EDAD"])
            if edad >= 18:
                sg.popup(f"{nombre}, eres mayor de edad.")
            else:
                sg.popup(f"{nombre}, eres menor de edad.")
        except ValueError:
            sg.popup("Por favor, ingresa una edad válida.")

window.close()