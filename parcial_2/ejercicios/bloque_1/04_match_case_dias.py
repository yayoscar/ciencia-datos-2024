dia = input("Introduce un día de la semana (en minúsculas): ")

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