import FreeSimpleGUI as sg
from funciones import calcular_ahorro
from funciones import calculadora

layout = [
    [sg.Text("Nombre del gasto:"), sg.Input(key="nombre")],
    [sg.Text("Precio por unidad:"), sg.Input(key="precio")],
    [sg.Text("Veces por semana:"), sg.Input(key="veces")],
    [sg.Text("Meses:"), sg.Input(key="meses")],
    [sg.Button("calcular ahorro")],
    [sg.Text("", key="resultado")]
]

window = sg.Window("Calculadora de gastos hormiga", layout)

calculadora(window)

