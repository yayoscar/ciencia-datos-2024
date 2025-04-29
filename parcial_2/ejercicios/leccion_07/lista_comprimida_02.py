# Realiza un ejericio que convierta los valores de texto a flotante
# salida:
# [1.23, 13.2, 2.78]

lista = ['1.23','13.2','2.78']
lista = [ float(elemento) for elemento in lista ]
print(lista)