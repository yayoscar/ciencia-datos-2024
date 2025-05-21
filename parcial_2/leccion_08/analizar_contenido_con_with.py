nombre_archivo = "oso.txt"
with open(nombre_archivo,"r") as archivo:
        contenido = archivo.read()

largo_contenido=len(contenido)
print(largo_contenido)