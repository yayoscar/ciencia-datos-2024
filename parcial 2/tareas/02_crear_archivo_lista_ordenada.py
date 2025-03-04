numeros_flotantes = [3.6,3.3,3.5,2.5,5.4,9.2]

numeros_flotantes.sort()

archivo = open("lista_ordenada.txt", "w")
archivo.write(",".join(str(orden) for orden in numeros_flotantes))
archivo.close()