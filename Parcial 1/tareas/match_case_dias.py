dia = input("Ingresa un dia de la semana: ")
match dia:
    case "lunes":
        print("Monday")
    case "martes":
        print("Tuesday")
    case "miercoles":
        print("Wednesday")
    case "jueves":
        print("Thursday")
    case "viernes":
        print("Friday")
    case "sabado":
        print("Saturday")
    case "domingo":
        print("Sunday")
    case " ":
        print("Dia invalido")
