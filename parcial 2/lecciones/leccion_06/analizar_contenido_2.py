nombre_archivo = "ensayo.txt"
archivo = open(nombre_archivo, "r")
contenido = archivo.read()
largo_contenido =len(contenido)
print(f"largo_contenido){largo_contenido} caracteres.")