
numeros = [3.14, 1.59, 2.65, 5.35, 4.28]


numeros.sort()


with open('orden.txt', 'w') as archivo:
    archivo.write(','.join(str(num) for num in numeros))
