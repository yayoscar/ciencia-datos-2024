
with open("historia.txt","r") as archivo:
    contenido = archivo.read()

with open("historia_copia.txt", "w") as copia:
    copia.write(contenido)