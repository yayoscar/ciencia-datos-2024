dia = input("Introduce un día de la semana (en minúsculas): ")

match dia:
    case "lunes":
        clasificacion = "Inicio de semana"
    case "miércoles":
        clasificacion = "Mitad de semana"
    case "sábado" | "domingo":
        clasificacion = "Fin de semana"
    case _:
        clasificacion = "Día normal"

print(f"El día '{dia}' pertenece a: {clasificacion}.")
