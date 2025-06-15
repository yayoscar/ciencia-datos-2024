import FreeSimpleGUI as sg
import csv
import funciones as cal

layout = [
    [sg.Text("Bienvenido a la calculadora de ahorros hormiga, porfavor rellena lo siguiente🥺🙏", font=("ROG fonts", 12))],
    [sg.Text("Nombre del gasto:"), sg.Input(key="NOMBRE")],
    [sg.Text("Ingresa el precio por unidad:"), sg.Input(key="PRECIO")],
    [sg.Text("las Veces por semana:"), sg.Input(key="VECES")],
    [sg.Text("cuantos Meses:"), sg.Input(key="MESES")],
    [sg.Button("presiona aqui para Calcular cuanto podrias ahorrar")],
    [sg.Text("Resultados:", font=("Arial", 12, "bold"))],
    [sg.Multiline(size=(50, 10), key="RESULTADO", disabled=True)]
]
ventana = sg.Window("Calculadora de ahorro hormiga", layout)
gastos = {}

while True:
    evento, valores = ventana.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "presiona aqui para Calcular cuanto podrias ahorrar":
        try:
            nombre = valores["NOMBRE"]
            precio = float(valores["PRECIO"])
            veces = int(valores["VECES"])
            meses = int(valores["MESES"])

            ahorro = cal.calcular_ahorro(precio, veces, meses)
            gastos[nombre] = round(ahorro, 2)

            resultado = ""
            total = 0
            for nombre_gasto, total_gasto in gastos.items():
                resultado += f"{nombre_gasto}: ${total_gasto:.2f}\n"
                total += total_gasto
            resultado += f"podrias ahorrar: ${total:.2f}, si evitas estos gastos por: {meses} Meses"

            ventana["RESULTADO"].update(resultado)

            with open("gastos_ahorro.csv", "a", newline="") as archivo:
                escribir = csv.writer(archivo)
                escribir.writerow([])
                escribir.writerow(["Este es el nombre del ahorro y la Cantidad que podiras ahorrar:"])

                for nombre_gasto, total_gasto in gastos.items():
                    escribir.writerow([nombre_gasto, total_gasto])
        except ValueError:
            sg.popup("Por favor, ingresa valores numéricos válidos en precio, veces y meses.")

ventana.close()

