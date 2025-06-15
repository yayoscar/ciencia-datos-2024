import FreeSimpleGUI as sg
from funciones import calcular_ahorro

layout = [
    [sg.Text("Nombre del gasto:"), sg.Input(key="nombre")],
    [sg.Text("Precio por unidad:"), sg.Input(key="precio")],
    [sg.Text("Veces por semana:"), sg.Input(key="veces")],
    [sg.Text("Meses:"), sg.Input(key="meses")],
    [sg.Button("Calcular ahorro")],
    [sg.Text("", key="resultado")]
]

window = sg.Window("Calculadora de gastos hormiga", layout)
window.close()
