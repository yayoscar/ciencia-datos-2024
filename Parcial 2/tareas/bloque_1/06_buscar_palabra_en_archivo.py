palabra = input("Escribe la palabra a buscar: ")
with open("texto.txt", "r") as archivo:
    contenido = archivo.read()
    conteo = contenido.lower().count(palabra.lower())
    print(f"La palabra aparece {conteo} veces.")