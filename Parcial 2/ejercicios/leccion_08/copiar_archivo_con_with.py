# Leer el archivo original
with open('historia.txt', 'r') as archivo_original:
    contenido = archivo_original.read()

# Crear una copia del archivo
with open('historia_copia.txt', 'w') as archivo_copia:
    archivo_copia.write(contenido)