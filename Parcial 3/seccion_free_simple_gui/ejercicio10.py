import FreeSimpleGUI as sg

layout = [
    [sg.Text("Número 1:"), sg.Input(key="NUM1")],
    [sg.Text("Número 2:"), sg.Input(key="NUM2")],
    [sg.Button("Sumar"), sg.Button("Restar"), sg.Button("Multiplicar"), sg.Button("Dividir")],
    [sg.Text("Resultado:"), sg.Text("", size=(15,1), key="RESULTADO")]
]

window = sg.Window("Calculadora", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    try:
        num1 = float(values["NUM1"])
        num2 = float(values["NUM2"])
        if event == "Sumar":
            resultado = num1 + num2
        elif event == "Restar":
            resultado = num1 - num2
        elif event == "Multiplicar":
            resultado = num1 * num2
        elif event == "Dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        window["RESULTADO"].update(resultado)
    except ValueError:
        sg.popup("Por favor, introduce números válidos.")

window.close()