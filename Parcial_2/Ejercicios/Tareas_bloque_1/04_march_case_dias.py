dia = input("ingresa un dia de la semana en minusculas: ")
match dia:
    case "domingo"|"sabado":
        print("fin de semana")
    case "lunes":
        print("inicio de semana")
    case "miercoles":
        print("mitad de la semana")
    case "martes"|"miercoles"|"jueves"|"viernes":
        print("dia normal")