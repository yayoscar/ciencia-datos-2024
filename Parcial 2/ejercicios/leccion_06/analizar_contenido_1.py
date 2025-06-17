nombre_archivo = "ensayo.txt"
archivo = open(nombre_archivo)
contenido = archivo.read()
largo_contenido = len(contenido)
print(largo_contenido)