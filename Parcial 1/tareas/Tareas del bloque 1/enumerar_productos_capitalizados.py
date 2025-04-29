def mostrar_productos():
    # Definir una lista de productos en minúsculas
    productos = ["manzana", "pera", "platano", "naranja", "sandia"]

    # Capitalizar cada producto
    productos_capitalizados = [producto.capitalize() for producto in productos]

    # Imprimir en el formato deseado
    for i, producto in enumerate(productos_capitalizados):
        print(f"{i}- {producto}.txt")

# Ejecutar función
mostrar_productos()
