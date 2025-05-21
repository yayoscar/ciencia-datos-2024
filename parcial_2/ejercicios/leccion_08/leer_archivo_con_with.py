'''archivo = open('oso.txt', 'r')
print(archivo.read())
archivo.close()'''
with open('osos.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)