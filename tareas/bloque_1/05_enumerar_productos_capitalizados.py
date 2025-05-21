
productos = ["manzana", "pera", "naranja", "plátano", "sandía"]

for i, producto in enumerate(productos):
    nombre_archivo = f"{producto.capitalize()}.txt"
    print(f"{i} - {nombre_archivo}")
