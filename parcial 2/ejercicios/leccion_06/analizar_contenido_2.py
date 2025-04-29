nombre_archivo="ensayo.txt"
archivo = open(nombre_archivo,"r")
contenido = archivo.read()
largo_contenido=len(contenido)
print(f"el archivo contiene{largo_contenido} caracteres")
