with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

palabra = input("Ingresa la palabra que deseas buscar: ")

conteo = contenido.lower().split().count(palabra.lower())

print(f"La palabra aparece {conteo} veces.")