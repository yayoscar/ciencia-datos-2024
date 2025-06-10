import FreeSimpleGUI as sg
from funciones import *

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")],
    [sg.Text("Tienda recomendada", key="TIENDA RECOMENDADA")],
    [sg.Text("ahorro", key="AHORRO")]
]

window = sg.Window("Proyecto 5", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Comparar precios":
        p1 = float(values["P1"])
        p2 = float(values["P2"])
        p3 = float(values["P3"])
        cantidad = (values["CANTIDAD"])

        tienda, ahorros = comparar_precios(p1, p2, p3, cantidad)

        window["RECOMENDACION"].update(f"Tienda recomendada: {tienda}")

        texto_ahorro = "\n".join([f"Ahorro de {t}: ${a}" for t, a in ahorros.items()])
        window["AHORRO"].update(texto_ahorro)

window.close()
