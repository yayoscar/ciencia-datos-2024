import FreeSimpleGUI as sg

layout = [
    [sg.Text("Número 1:"), sg.Input(key="NUM1")],
    [sg.Text("Número 2:"), sg.Input(key="NUM2")],
    [sg.Button("Sumar")],
    [sg.Text("Resultado:"), sg.Text("", key="RESULTADO")]
]

window = sg.Window("Calculadora Suma Simple", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,):
        break
    elif event == "Sumar":
        try:
            num1 = float(values["NUM1"])
            num2 = float(values["NUM2"])
            resultado = num1 + num2
            window["RESULTADO"].update(str(resultado))
        except ValueError:
            sg.popup("Por favor, introduce números válidos.")

window.close()
