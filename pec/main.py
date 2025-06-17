import FreeSimpleGUI as sg
import csv
from funciones import precios_comparados

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")],
    [sg.Output(size=(60, 10))]
]

window = sg.Window("Comparador de Precios", layout)

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
                if values[key]:
                    precios.append(float(values[key]))
                else:
                    precios.append(float('inf'))

            totales = [p * cantidad for p in precios]
            tienda_recomendada = totales.index(min(totales)) + 1
            ahorro = max(totales) - min(totales)

            print(f"Tienda mas barata es: Tienda {tienda_recomendada} con un total de : ${min(totales):.2f})")
            print(f"Ahorro comparado con más cara: ${ahorro:.2f}")
            print(precios_comparados(precios))

            with open("datos.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([producto, *precios, cantidad, tienda_recomendada, ahorro])
        except Exception as pec:
            print("Error en los datos ingresados. Asegúrate de llenar todos los campos correctamente.")
            print(str(pec))

window.close()