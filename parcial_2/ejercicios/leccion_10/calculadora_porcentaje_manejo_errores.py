try:
    valor_total = float(input("Ingresa tu valor total: "))
    valor = float(input("Ingresa tu segundo vallor: "))
    porcentaje = valor/valor_total * 100
    print(f"Eso es {porcentaje}%")
except ValueError:
    print("Debes ingresar un número, inténtalo de nuevo")