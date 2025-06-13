import FreeSimpleGUI as sg
from funciones import calcular

layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="n")],
    [sg.Text("Precio por unidad:"),sg.Input(key="p")],
    [sg.Text("Veces por semana"), sg.Input(key="v")],
    [sg.Text("Meses:"), sg.Input(key="m")],
    [sg.Button("Calcular ahorro")]
]

window =sg.Window("Calculadora de gastos hormiga",layout,font=("Arial",15),background_color="pink",button_color="purple",sbar_background_color="purple")

print(calcular("p","v","m"))
window.read()
window.close()