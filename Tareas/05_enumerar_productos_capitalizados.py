productos = ['manzana', 'banana', 'pera', 'naranja', 'uva']
productos_capitalizados = [producto.capitalize() for producto in productos]
for indice, producto in enumerate(productos_capitalizados):
    print(f"{indice} - {producto}.txt")
