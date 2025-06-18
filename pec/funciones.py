import csv

def registro(producto_a_comprar, precios, cantidad_producto, mejor_opción, ahorro_de_compra):
    with open("datos.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([producto_a_comprar, *precios, cantidad_producto, mejor_opción, ahorro_de_compra])