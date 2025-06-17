with open("historia.txt") as archivo:
    contenido = archivo.read()

with open("historia_copia.txt", "w") as archivo:
    archivo.write(contenido)