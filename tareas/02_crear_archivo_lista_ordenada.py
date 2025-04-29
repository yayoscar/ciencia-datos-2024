numeros = [8.5,9.9,5.5,4.5,1.5]
numeros.sort()
archivo = open("orden.txt", "m")
archivo.write(",".join(str(n)for n in numeros))
archivo.close()