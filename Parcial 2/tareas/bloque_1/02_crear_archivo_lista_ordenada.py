numeros = [1.5, 12.0, 0.67, 4.4, 34.0]
numeros.sort()
with open ("orden.txt", "w") as archivo:
    archivo.write(", ".join(map(str, numeros)))