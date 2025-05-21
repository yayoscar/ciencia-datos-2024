def calcular_promedio():
    numeros = []
    for i in range(3):
        while True:
            try:
                num = float(input(f"Ingresa el número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada no válida. Ingresa un número válido.")

    promedio = sum(numeros) / len(numeros)
    print(f"El promedio de los tres números es: {promedio:.2f}")

if __name__ == "__main__":
    calcular_promedio()
    #Daniela Beatriz Chin Morales
