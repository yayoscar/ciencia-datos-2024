
lista =['1.python','2.java','3.golang']
lista = [elemento.replace( '.',   '_') +'.txt' for elemento in lista ]
print(lista)