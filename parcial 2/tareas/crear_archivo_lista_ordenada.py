numeros = [8.4, 3.2, 5.7, 1.1, 9.0]
numeros.sort()

archivo = open("orden.txt", "w")
for i in range(len(numeros)):
    archivo.write(str(numeros[i]))
    if i < len(numeros) - 1:
        archivo.write(", ")
archivo.close()
