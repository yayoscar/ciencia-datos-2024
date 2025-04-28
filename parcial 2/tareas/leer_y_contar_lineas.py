archivo = open("parrafo.txt", "r")
contador = 0
linea = archivo.readline()
while linea != "":
    contador += 1
    linea = archivo.readline()
archivo.close()

print(f"El archivo tiene {contador} líneas.")
