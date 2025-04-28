def match_case_dias():
    dia = input("ingrese un dia de la semana (en minusculas porfis): ")
    match dia:
        case "lunes":
            print("inicio de semana pipipipipi")
        case "miercoles":
            print("mitad de semana, ya mero te hechas tus cheves")
        case "sábado" | "domingo":
            print("fin de semana, chambabu chambabu")
        case _:
            print("dia normalon")
match_case_dias()