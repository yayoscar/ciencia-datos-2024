dia = input("Introduce un dia de la semana (en minúsculas): ")
match dia:
    case "lunes":
        print("inicio de semana")
    case "miercoles":
        print("mitad de semana")
    case "sabado":
        print("fin de semana")
    case "martes":
        print("dia comun")
    case _:
        print("dia no existente")