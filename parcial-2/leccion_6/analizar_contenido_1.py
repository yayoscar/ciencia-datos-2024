archivo = open("ensayo.txt","r")
contenido = archivo.read()
archivo.close()

caracteres = len(contenido)
print(caracteres)