lista = ['1.python', '2.patricio', '3.VSC']
lista = [elemento.replace('.', '-') + '.txt' for elemento in lista]
print(lista)