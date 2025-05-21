productos = ["manzana", "leche", "pan", "queso", "jugo"]

productos_capitalizados = [producto.capitalize() for producto in productos]


for i, producto in enumerate(productos_capitalizados):
    print(f"{i} - {producto}.txt")