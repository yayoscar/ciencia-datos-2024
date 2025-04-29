numeros = [4.7, 1.2, 9.8, 3.5, 7.3]
numeros_ordenados = sorted(numeros)

with open("orden.txt", "w") as archivo:
    archivo.write(",".join(map(str, numeros_ordenados)))
print("Los números ordenados han sido escritos en orden.txt")
