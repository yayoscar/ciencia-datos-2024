numeros = [9.9,8.7,5.6,3.5,2.1]
numeros_ordenados= sorted(numeros)
archivo = open("archivo.txt", "w")
archivo.write(", ".join(str(num)for num in numeros_ordenados))
print("los numeros se han guardado ordenadamente en 'orden.txt'.")