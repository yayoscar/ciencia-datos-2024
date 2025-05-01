lista = ['1.python', '2.java', '3.golang']
lista = [elemento.replace('.', '-') + '.txt' for elemento in lista]
print(lista)
'''for elemento in lista:
    elemento.replace('.', '-')
    elemento = elemento + '.txt'

print(lista)'''