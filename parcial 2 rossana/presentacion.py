def calcular_promedio():
    materias = []
    num = int(input("¿Cuántas materias deseas ingresar?: "))

    for i in range(num):

        print(f"\nMateria {i+1}:")
        nombre = input("Nombre: ")
        calificacion = float(input("Calificación (0-10): "))
        peso_input = input("Peso (opcional, enter para 1): ")
        peso = float(peso_input) if peso_input else 1.0

        materias.append({
            "nombre": nombre,
            "calificacion": calificacion,
            "peso": peso
        })

    total_peso = sum(m["peso"] for m in materias)
    suma_ponderada = sum(m["calificacion"] * m["peso"] for m in materias)
    promedio = suma_ponderada / total_peso

    print("\n=== RESULTADO ===")
    print(f"Promedio final: {promedio:.2f}")
    if promedio >= 6.0:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")


if __name__ == "__main__":
    print("Bienvenido a la Calculadora de Promedios.")
    calcular_promedio()
