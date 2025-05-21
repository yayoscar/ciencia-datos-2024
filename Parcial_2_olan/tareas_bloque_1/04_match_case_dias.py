dia= input("ingresa un dia de la semana en minusculas para clasificarlo:  ")
match dia:
    case "Lunes"| "lunes":
        print("Inicio de semana")
    case "Miercoles"| "miercoles":
        print("Mitad de semana")
    case "Jueves"|"jueves":
        print("mitad de semana")
    case "Sabado"|"sabado":
        print(" fin de semana")
    case "Domingo"|"domingo":
        print("fin de semana")
    case _:
        print("Día normal")