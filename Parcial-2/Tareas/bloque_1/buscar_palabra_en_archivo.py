#  La palabra mas repetida dentro el archivo es: "como"
palabra = input("Escribe la palabra que deseas buscar: ")
with open("texto.txt", "r") as archivo:
    contenido = archivo.read()
    cantidad = contenido.lower().count(palabra.lower())
print(f"La palabra aparece {cantidad} veces.")