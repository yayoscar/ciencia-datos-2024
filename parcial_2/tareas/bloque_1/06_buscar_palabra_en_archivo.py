palabra = input("Introduce una palabra para buscar en el archivo: ")
with open("texto.txt", "r") as archivo:
    contenido_texto = archivo.read()
    número_veces = contenido_texto.lower().count(palabra.lower())
print(f"La palabra aparece {número_veces} veces.")