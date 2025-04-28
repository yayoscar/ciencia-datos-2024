lista = [3.2, 1.5, 7.8, 0.4, 5.9]
lista.sort()
texto = ",".join(str(n) for n in lista)
archivo = open("orden.txt", "w")
archivo.write(texto)
archivo.close()