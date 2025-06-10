import FreeSimpleGUI as sg
import csv

layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
    [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen")]
]

window = sg.Window("Registro de Gastos y Categorías", layout, font=('Arial', 25))

while True:
    evento, values = window.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == "Guardar gasto":
        Monto = values["MONTO"]
        Categoria = values["CATEGORIA"]
        Fecha = values["FECHA"]

        with open("datos.csv", "a", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([f"El monto es de: {Monto}"])
            writer.writerow([f"La categoría es: {Categoria}"])
            writer.writerow([f"La fecha es: {Fecha}"])

window.close()

