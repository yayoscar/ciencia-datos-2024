with open("historia.txt", "r") as original:
    contenido = original.read()

with open("historia_copia.txt", "w") as copia:
    copia.write(contenido)