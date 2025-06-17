numeros = [3.4, 1.2, 5.6, 2.1, 4.8]
numeros.sort()
with open("orden.txt", "w") as archivo:
    archivo.write(",".join(str(num) for num in numeros))