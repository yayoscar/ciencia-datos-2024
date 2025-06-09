import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Verificar"), sg.Button("Salir")]
]

window = sg.Window("Verificar Edad", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Verificar":
        try:
            edad = int(values["EDAD"])
            if edad >= 18:
                sg.popup("Eres mayor de edad.")
            else:
                sg.popup("Eres menor de edad.")
        except ValueError:
            sg.popup("Ingresa una edad válida (número entero).")

window.close()