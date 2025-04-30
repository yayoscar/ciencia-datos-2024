productos = ["arroz","leche","avena","miel"]
productos = [producto.capitalize() for producto in productos]
for indice, producto in enumerate(productos):
    print(f"{indice} : {producto}")
