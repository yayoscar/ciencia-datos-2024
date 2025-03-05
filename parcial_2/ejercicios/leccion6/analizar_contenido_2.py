archivo = open("ensayo.txt","r")
contenido = archivo.read()
largo_contenido = len(contenido)
print(f"El archivo contiene {largo_contenido} caracteres")
