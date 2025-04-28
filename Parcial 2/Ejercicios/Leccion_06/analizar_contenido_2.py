nombre_archivo="ensayo.txt"
archivo = open("ensayo.txt")
contenido = archivo.read()
largo_contenido=len(contenido)
print(f"El archivo contiene {largo_contenido} caracteres.")
