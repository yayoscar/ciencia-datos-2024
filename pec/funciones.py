import csv
import os

# Nombre del  CSV
FILENAME = 'comparaciones.csv'

# Crear archivo CSV
def crear_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)


# Comparar precios entre tiendas
def comparar(producto, cantidad, precio1, precio2):

    return producto, cantidad, "", 0, 0


# Guardar
