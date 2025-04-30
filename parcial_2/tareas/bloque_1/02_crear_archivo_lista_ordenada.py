numeros = [3.14, 1.59, 2.65, 5.35, 9.79]
numeros.sort()
archivo = open("orden.txt", "w")

for i in range(len(numeros)):
    archivo.write(str(numeros[i]))
    if i < len(numeros) - 1:
        archivo.write(", ")
archivo.close()