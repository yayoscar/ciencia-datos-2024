def promedio_alumnos():
    try:
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Ingrese la nota del alumno {i}: "))
            notas.append(nota)
        promedio = sum(notas) / len(notas)
        print(f"El promedio de los 3 alumnos es: {promedio:.2f}")
    except ValueError:
        print("Error: Asegúrate de ingresar números válidos.")

# Ejemplo de uso
promedio_alumnos()
