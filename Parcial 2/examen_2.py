def calcular_promedio(cantidad):
    suma = 0
    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        suma += numero
    promedio = suma / cantidad
    return promedio


# Programa principal
repetir = "si"

while repetir.lower() == "si":
    cantidad = int(input("¿Cuántos números desea ingresar? "))
    if cantidad > 0:
        promedio = calcular_promedio(cantidad)
        print(f"El promedio de los números ingresados es: {promedio}")
    else:
        print("La cantidad debe ser mayor que 0.")

    repetir = input("¿Desea realizar otro cálculo? (si/no): ")

print ("Gracias por tus proprcionar tus numeros")
