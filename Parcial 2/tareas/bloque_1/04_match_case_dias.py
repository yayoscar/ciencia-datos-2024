dia = input("Ingresas un día de la semana (en minúsculas): ")
match dia:
    case "lunes":
        print("Inicio de semana")
    case "miércoles":
        print("Mitad de semana")
    case "sábado"|"domingo":
        print("Fin de semana")
    case _:
        print("Día normal")