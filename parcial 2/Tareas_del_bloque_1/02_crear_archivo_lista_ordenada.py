numeros = [5.3, 2.3,4.4,5.9,3.3]
numeros.sort()
with open("orden.txt", "w") as archivo:
    archivo.write(",".join(str(num) for num in numeros))