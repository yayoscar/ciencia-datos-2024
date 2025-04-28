dia = input("ingresa un dia de la semana en minisculas: ")

match dia:
    case "lunes":
        print("inicio de semana")

    case "miercoles":
        print("mitad de la semana ")

    case "sabado"|"domingo":
        print("fin de semana")
    case _:
        print("dia nomrmal")