
def verificar_numero():
    try:
        numero = float(input("Ingresa un número: "))
        if numero > 0:
            print(f"El número {numero} es positivo.")
        elif numero < 0:
            print(f"El número {numero} es negativo.")
        else:
            print("El número es cero.")
    except ValueError:
        print("Por vafor ingresar un número válido.")

verificar_numero()