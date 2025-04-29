import random

numeros = [random.uniform(0, 10) for _ in range(5)]
numeros.sort()

with open("orden.txt", "w") as archivo:
    archivo.write(",".join(str(numero) for numero in numeros))
