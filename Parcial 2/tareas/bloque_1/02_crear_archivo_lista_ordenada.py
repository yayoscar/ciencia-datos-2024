numeros = [0.459,9.573,2.783,6.549,4.596]
numeros.sort()
with open("orden.txt", "w") as archivo:
  archivo.write(",".join(str(numero) for numero in numeros))