# Abrir el archivo en modo lectura
with open('oso.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()

# Imprimir el contenido del archivo
print(contenido)