numeros = [3.14, 1.59, 2.71, 0.99, 4.20]

numeros_ordenados = sorted(numeros)

with open("orden.txt", "w") as archivo:
    archivo.write(",".join(str(num) for num in numeros_ordenados))