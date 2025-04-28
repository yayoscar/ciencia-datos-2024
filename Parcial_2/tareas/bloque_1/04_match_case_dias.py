dia = input("Escribe un día de la semana: ")

match dia:
    case "lunes":
        print("Inicio de semana")
    case "miércoles":
        print("Mitad de semana")
    case "sábado" | "domingo":
        print("Fin de semana")
    case _:
        print("Día normal")
