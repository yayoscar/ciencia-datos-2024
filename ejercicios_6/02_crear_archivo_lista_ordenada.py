numeros = [9.9,8.7,5.6,3.4,40.4]
numeros_ordenados = sorted(numeros)
archivo = open("archivo.txt","w")
archivo.write(", ".join(str(num)for num in numeros_ordenados))
print("los numeros an sido guardado ordenadamente en 'orden.txt'.")