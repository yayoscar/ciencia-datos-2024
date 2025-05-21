def verificar_numero():
    try:
        numero = float(input("ingresa un numero"))
        if numero > 0:
            print(f"el numero{numero}es positivo.")
        elif numero < 0:
            print(f"el numero{numero}es negtivo.")
        else:
            print("el numero es cero")
    except ValueError:
        print("porfavor ingresar un numero valido")
verificar_numero()