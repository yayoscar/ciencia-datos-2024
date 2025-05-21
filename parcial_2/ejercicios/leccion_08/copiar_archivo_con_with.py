with open('historia.txt', 'r') as archivo:
    contenido = archivo.read()
with open('historia_copia.txt', 'w') as archivo:
    archivo.write(contenido)