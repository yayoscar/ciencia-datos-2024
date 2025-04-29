productos = ["manzana", "naranja", "plátano", "uvas", "mango"]

for indice, producto in enumerate(productos):
    nombre_archivo = f"{indice} - {producto.capitalize()}.txt"
    print(nombre_archivo)
