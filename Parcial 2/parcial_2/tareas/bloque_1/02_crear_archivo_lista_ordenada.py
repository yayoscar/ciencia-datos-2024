lista = [8.5, 3.2, 10.1, 5.7, 1.9]
lista_ordenada = sorted(lista)
archivo = open("orden.txt", "w")
archivo.write(",".join(map(str, lista_ordenada)))
archivo.close()
print("Lista ordenada:", lista_ordenada)
