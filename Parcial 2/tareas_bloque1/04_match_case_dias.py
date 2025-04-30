dia = input("Ingresa un día de la semana(en minúsculas): ")
match dia:
        case "domingo"|"sábado":
            print("Fin de semana")
        case "lunes":
            print("Inicio de semana")
        case "miércoles":
            print("Mitad de semana")
        case "martes"|"jueves"|"viernes":
            print("Día normal")
