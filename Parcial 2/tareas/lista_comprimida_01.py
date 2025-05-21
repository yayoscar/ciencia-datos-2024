lista = ['1.python','2.java','3.golang']

#Imprime la lista en el siguiente formato,utilizando listas comprimidas
#('1-python.txt','2-java,txt´,'3-golang,txt')

lista = [elemento.replace('.','-')+'txt' for elemento in lista]
print(lista)