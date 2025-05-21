
numeros = [3.14, 1.618, 2.718, 0.577, 4.669]
numeros.sort()

with open("orden.txt", "w") as archivo:
    archivo.write(", ".join(str(num) for num in numeros))

print("Los números ordenados se han guardado en 'orden.txt'")
