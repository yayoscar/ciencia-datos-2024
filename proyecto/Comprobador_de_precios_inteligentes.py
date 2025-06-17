import FreeSimpleGUI as sg
import csv
from datetime import datetime

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3 (opcional):"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")],
    [sg.Multiline(size=(60, 6), key="RESULTADO", disabled=True)]
]

window = sg.Window("Comparador de Precios Inteligente", layout)

def guardar_csv(producto, precios, cantidad, tienda_ganadora, ahorro):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("comparacion_precios.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([fecha, producto, *precios, cantidad, tienda_ganadora, ahorro])

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Comparar precios":
        try:
            producto = values["PRODUCTO"]
            cantidad = int(values["CANTIDAD"])

            precios = []
            for key in ["P1", "P2", "P3"]:
                precio = values[key]
                if precio.strip() != "":
                    precios.append(float(precio))
                else:
                    precios.append(None)

            totales = []
            for precio in precios:
                if precio is not None:
                    totales.append(precio * cantidad)
                else:
                    totales.append(None)

            tiendas_validas = [(i+1, total) for i, total in enumerate(totales) if total is not None]

            tienda_ganadora = min(tiendas_validas, key=lambda x: x[1])
            tienda_mas_cara = max(tiendas_validas, key=lambda x: x[1])

            resultado = (
                f"Tienda recomendada: Tienda {tienda_ganadora[0]} (total: ${tienda_ganadora[1]:.2f})\n"
                f"Ahorro comparado con más cara: ${tienda_mas_cara[1] - tienda_ganadora[1]:.2f}"
            )
            window["RESULTADO"].update(resultado)

            guardar_csv(producto, precios, cantidad, f"Tienda {tienda_ganadora[0]}", f"${tienda_mas_cara[1] - tienda_ganadora[1]:.2f}")

        except ValueError:
            sg.popup_error("Error: Verifica que todos los precios y la cantidad sean números válidos.")

window.close()