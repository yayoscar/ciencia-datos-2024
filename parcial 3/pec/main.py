import FreeSimpleGUI as sg
from funciones import comparar_precios

layout = [
    [sg.Text("Comparador de Precios", font=("Arial", 16))],
    [sg.Text("Producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precios:")],
    [sg.Text("Tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar"), sg.Button("Salir")],
    [sg.Multiline(size=(40, 6), key="RESULTADO")]
]

window = sg.Window("Comparador de Precios", layout)

while True:
    event, values = window.read()
    if event == "Salir" or event == sg.WINDOW_CLOSED:
        break
    if event == "Comparar":
        resultado = comparar_precios(values)
        window["RESULTADO"].update(resultado)

window.close()