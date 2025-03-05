dia= input("ingresa un dia de la semana en minusculas para clasificarlo:  ")
match dia:
    case "Lunes"| "lunes":
        print("Inicio de semana")
    case"Martes"| "martes":
        print("inicio de semana")
    case "Miercoles"| "miercoles":
        print("entre semana")
    case "Jueves"|"jueves":
        print("entre semana")
    case "Sabado"|"sabado":
        print(" fin de semana")
    case "Domingo"|"domingo":
        print("fin de semana")
    case _:
        print("Día tranquilo")