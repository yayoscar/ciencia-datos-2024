archivo = open("ensayo.txt","r")
contenido = archivo.read()
largo_contenido=len(contenido)
print(f"el archivo contiene {largo_contenido}caracteres.")