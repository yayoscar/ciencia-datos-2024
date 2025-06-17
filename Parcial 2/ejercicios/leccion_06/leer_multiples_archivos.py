nombres_archivo = ['a.txt', 'b.txt', 'c.txt']

for nombre in nombres_archivo:
    archivo = open(nombre, "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()