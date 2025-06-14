import csv

def guardar_gasto(monto, categoria, fecha):

    monto = float(monto)

    with open("datos.csv", "a", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([monto, categoria, fecha])

    return "Gasto guardado correctamente."


def leer_datos():
    datos = []
    with open("datos.csv", newline='') as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if len(fila) == 3:
                datos.append(fila)
    return datos


def mostrar_resumen():
    datos = leer_datos()
    comida = 0.0
    transporte = 0.0
    otro = 0.0

    for fila in datos:
        monto_str, categoria, _ = fila
        monto = float(monto_str)

        if categoria == "Comida":
            comida += monto
        elif categoria == "Transporte":
            transporte += monto
        else:
            otro += monto

    total = comida + transporte + otro
    resumen = f"""Resumen de Gastos:
- Comida:       ${comida:.2f}
- Transporte:   ${transporte:.2f}
- Otros:        ${otro:.2f}
-------------------------
- Total:        ${total:.2f}
"""
    return resumen

