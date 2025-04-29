lista_de_números_desordenados=[17.56,13.05,18.10,14.09,25.01]
lista_de_números_desordenados.sort()
archivo = open('orden.txt', 'w')
for list in lista_de_números_desordenados:
    archivo.write(f"{list}\n")
archivo.close()
print (lista_de_números_desordenados)