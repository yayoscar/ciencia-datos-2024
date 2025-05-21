def suma(n1, n2):
    try:
        resultado = n1 + n2
        return resultado
    except TypeError:
        return "Error: Asegúrate de ingresar números válidos."

# Ejemplo de uso
a = 10
b = 5
print("La suma es:", suma(a, b))
