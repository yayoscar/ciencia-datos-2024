numeros = [3.14, 1.68, 9.81, 2.71, 0.99]
numeros_ordenados = sorted(numeros)
contenido = ",".join(str(num) for num in numeros_ordenados)
with open("orden.txt", "w") as archivo:
    archivo.write(contenido)
print("Números ordenados guardados en 'orden.txt'")