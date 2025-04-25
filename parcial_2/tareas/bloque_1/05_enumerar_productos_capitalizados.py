productos = ["productouno", "productodos", "productotres", "productocuatro", "productocinco"]
productos_capitalizados = [producto.capitalize() for producto in productos]
for i, producto in enumerate(productos_capitalizados):
    print(f"{i} - {producto}.txt")
