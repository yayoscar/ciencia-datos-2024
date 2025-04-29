palabra = input("Introduce una palabra para buscar en el archivo: ")

with open("texto.txt", "r") as archivo:
    contenido = archivo.read()
    cantidad = contenido.lower().count(palabra.lower())

print(f"La palabra aparece {cantidad} veces.")
