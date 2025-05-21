archivo=open("archivo.txt")
contenido=archivo.read()
print(contenido)
archivo.close()

archivo=open("archivo.txt","w")
archivo.write("hola mundo")
archivo.close()


archivo=open("archivo.txt","a")
archivo.write("\nhola mundo de nuevo")
archivo.close()