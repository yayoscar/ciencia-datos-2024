lista = ['1.phyton','2.java','3.golang']

#imprime la lista en el siguiente formato,utilizando lista comprimida
#['1.phyton','2.java','3.golang']

lista = [elemento.replace('.','-') + '.txt' for elemento in lista]
print(lista)