import random
lista = [random.randint(1, 2) for _ in range(10)]
print("Elementos multiplicados por 2:")
for numero in lista:
    resultado = numero * 2
    print(resultado)