archivo = open("ensayo.txt", "r")
contenido = archivo.read()
archivo.close()

contenido_modificado = contenido.title()

print(contenido_modificado)