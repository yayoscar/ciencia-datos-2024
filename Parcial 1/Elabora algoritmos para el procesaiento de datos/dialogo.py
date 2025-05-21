def suma(n1, n2):
    try:
        resultado = n1 + n2
        return resultado
    except TypeError:
        return "Error: Asegúrate de ingresar números válidos."


# Función para realizar un diálogo con el usuario
def dialogo():
    try:
        nombre = input("¿Cómo te llamas? ")
        edad = int(input("¿Cuántos años tienes? "))
        ciudad = input("¿Dónde vives? ")
        hobby = input("¿Cuál es tu pasatiempo favorito? ")

        print(f"Encantado de conocerte, {nombre}. Tienes {edad} años, vives en {ciudad} y te gusta {hobby}.")
    except ValueError:
        print("Error: Asegúrate de ingresar datos correctos.")


# Ejemplo de uso
a = 10
b = 5
print("La suma es:", suma(a, b))

dialogo()
_