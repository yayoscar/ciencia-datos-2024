nombres_archivo = ['a.txt', 'b.txt', 'c.txt']
for nombre_archivo in nombres_archivo:
    archivo = open(nombre_archivo,"r")
    print(archivo.read())
    archivo.close()
