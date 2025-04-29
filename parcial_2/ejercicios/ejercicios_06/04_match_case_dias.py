
dia = input("ingresa un dia de la semana en (en minusculas): ")
match dia:
    case "domingo"|"sabado":
        print("fin de semana")
    case "lunes":
        print("inicio de semana")
    case "miercoles":
        print("mitad de semana")
    case "martes" |"jueves"|"viernes":
        print("dia normal")

