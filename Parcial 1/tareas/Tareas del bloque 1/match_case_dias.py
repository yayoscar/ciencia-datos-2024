def clasificar_dia():
    # Solicitar un día en minúsculas
    dia = input("Ingresa un día de la semana (en minúsculas): ")

    # Clasificar el día usando match-case
    match dia:
        case "lunes":
            print("Inicio de semana")
        case "miércoles":
            print("Mitad de semana")
        case "sábado" | "domingo":
            print("Fin de semana")
        case "martes" | "jueves" | "viernes":
            print("Día normal")
        case _:
            print("Día no reconocido")

# Ejecutar función
clasificar_dia()
