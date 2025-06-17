import FreeSimpleGUI as sg
from funcionessofi import *

def main():
    layout = [
        [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="NOMBRE")],
        [sg.Text("Precio por unidad:"), sg.Input(key="PRECIO")],
        [sg.Text("Veces por semana:"), sg.Input(key="VECES")],
        [sg.Text("Meses:"), sg.Input(key="MESES")],
        [sg.Button("Calcular ahorro")],
        [sg.Text("", key="RESULTADO")]
    ]

    window = sg.Window("Calculadora de Gastos Hormiga", layout)

    while True:
        event, values = window.read()
        if event == "Calcular ahorro":
            try:
                gasto_total = calcular_gasto(values)
                resultado = mostrar_resultado(values, gasto_total)

                window["RESULTADO"].update(resultado)
                guardar_resultado(values, gasto_total)
            except ValueError:
                window["RESULTADO"].update("Error: Por favor, ingresa valores válidos.")
        elif event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
