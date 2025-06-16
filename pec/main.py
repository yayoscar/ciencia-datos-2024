import FreeSimpleGUI as sg
from funciones import comparar_precios

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")],
    [sg.Text("", key="TIENDA RECOMENDADA")],
    [sg.Text("", key="AHORRO")]
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
        cantidad = int(values["CANTIDAD"])

        tienda, total, ahorro = comparar_precios(p1, p2, p3, cantidad)

        window["TIENDA RECOMENDADA"].update(f"Tienda recomendada: {tienda} (total: ${int(total)})")
        window["AHORRO"].update(f"Ahorro comparado con más cara: ${int(ahorro)}")
    with open("datos.csv", "w") as archivo:
        archivo.write(f"Tienda recomendada: {tienda} (total: ${int(total)})\n")
        archivo.write(f"Ahorro comparado con más cara: ${int(ahorro)}\n")
window.close()

