import csv

def calcular_ahorro(precio, veces_por_semana, meses):
    """
    Calcula el ahorro total si se elimina un gasto hormiga durante un tiempo dado.
    """
    semanas_totales = meses * 4.33  # 4.33 semanas promedio por mes
    total = precio * veces_por_semana * semanas_totales
    return round(total, 2)

def guardar_datos(nombre, precio, veces, meses, ahorro, archivo="datos.csv"):
    """
    Guarda los datos del cálculo en un archivo CSV.
    """
    with open(archivo, mode="a", newline='', encoding="utf-8") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow([nombre, precio, veces, meses, ahorro])
