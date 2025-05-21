"""
Realiza un ejercicio que regrese una lista con el largo de los elementos
cadenas de la lista original
"""
lista = ['Oscar','Cristina','Alberto','Antonio','Juan']
# [5, 8, 7, 7, 4]
lista = [len(elemento) for elemento in lista]
print(lista)