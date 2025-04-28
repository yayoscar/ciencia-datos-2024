
def suma (n1, n2):
    return n1 + n2

try:
    n1 = float(input("Introduce el número n1: "))
    n2 = float(input("Introduce el número n2: "))
    resultado=suma(n1,n2)
    print("El resultado de la suma es ", resultado)
except ValueError:
    print("Entrada inválida. Por favor, introduzca números.")
