def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio

def main():
    calificaciones = [10, 9, 8, 7, 9, 6, 5, 8]
    promedio = calcular_promedio(calificaciones)
    print(f"Las calificaciones son: {calificaciones}")
    print(f"El promedio es: {promedio:.2f}")

if __name__ == "__main__":
    main()
