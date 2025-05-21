archivo=open('archivo.txt', 'r')
contenido=archivo.read()
print(contenido)
archivo.close()

archivo=open('archivo.txt', 'w')
archivo.write("Hola mundo")
archivo.close()

archivo=open('archivo.txt', 'a')
archivo.write("Hola mundo de nuevo")
