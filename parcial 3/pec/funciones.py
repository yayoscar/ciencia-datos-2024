import csv
from datetime import datetime

def comparar_precios(values):
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
            f"Tienda recomendada: Tienda {tienda_ganadora[0]}\n"
            f"Total: ${tienda_ganadora[1]:.2f}\n"
            f"Ahorro comparado con más cara: ${tienda_mas_cara[1] - tienda_ganadora[1]:.2f}"
        )
        guardar_csv(producto, precios, cantidad, f"Tienda {tienda_ganadora[0]}", f"${tienda_mas_cara[1] - tienda_ganadora[1]:.2f}")
        return resultado
    except ValueError:
        return "Error: Verifica que todos los precios y la cantidad sean números válidos."

def guardar_csv(producto, precios, cantidad, tienda_ganadora, ahorro):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("comparacion_precios.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([fecha, producto, *precios, cantidad, tienda_ganadora, ahorro])