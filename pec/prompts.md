utilice chat gtp
Crea un nuevo archivo llamado, por ejemplo:
funciones.py

En ese archivo, coloca todas las funciones que usas en tu programa. Por ejemplo:

# funciones.py

def calcular_gasto(precio, veces_por_semana, meses):
    total = precio * veces_por_semana * 4 * meses
    return total

def guardar_en_csv(nombre_gasto, total, archivo='datos.csv'):
    import csv
    with open(archivo, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nombre_gasto, total])