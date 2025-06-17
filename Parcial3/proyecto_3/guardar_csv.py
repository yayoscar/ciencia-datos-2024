import csv
#Ya aquí guardamos lo que vendría siendo los gastos de la persona, osea sus datos.
def guardar_resultado(nombre_gasto, precio_unidad, veces_por_semana, meses, ahorro, archivo="gastos_hormiga.csv"):
    try:
        with open(archivo, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([nombre_gasto, precio_unidad, veces_por_semana, meses, ahorro])
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")