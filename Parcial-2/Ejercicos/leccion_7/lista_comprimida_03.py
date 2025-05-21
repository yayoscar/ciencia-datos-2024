"""
realiza un ejercicio de una lista de numero, cree una nueva
con el valor al doble de sus elementos
"""

lista = [1, 2, 3, 4]
#[2,4,6,8]
lista = [elemento * 2 for elemento in lista]
print(lista)