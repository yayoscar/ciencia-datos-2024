import FreeSimpleGUI as sg
import funciones as cal

layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="NOMBRE")],
    [sg.Text("Precio por unidad:"), sg.Input(key="PRECIO")],
    [sg.Text("Veces por semana:"), sg.Input(key="VECES")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Button("Calcular ahorro")],
    [sg.Text("Resultados:", font=("Arial", 12, "bold"))],
    [sg.Multiline(size=(50, 10), key="RESULTADO", disabled=True)]
]
ventana = sg.Window("Calculadora de ahorro hormiga", layout)
gastos = {}
while True:
    evento, valores = ventana.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Calcular ahorro":
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
            resultado += f"Total: ${total:.2f}"

            ventana["RESULTADO"].update(resultado)
           
