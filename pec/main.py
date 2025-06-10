import FreeSimpleGUI as sg
from funciones import crear_csv, comparar

crear_csv()

layout = [
    [sg.Text("Producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Cantidad:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar"), sg.Button("Salir")],
    [sg.Text("", size=(50,3), key="RESULTADO")]
]

window = sg.Window("Comparador de Precios", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Comparar":
        try:
            producto = values["PRODUCTO"]
            p1 = float(values["P1"])
            p2 = float(values["P2"])
            cantidad = int(values["CANTIDAD"])

        except:
            sg.popup("Revisa los datos, deben ser números válidos.")

window.close()
