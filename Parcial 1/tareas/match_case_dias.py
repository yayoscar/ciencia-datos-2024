dia = input("Ingresa un día de la semana: ")

match dia.lower():
    case "lunes":
        print("Monday")
    case "martes":
        print("Tuesday")
    case "miércoles":
        print("Wednesday")
    case "jueves":
        print("Thursday")
    case "viernes":
        print("Friday")
    case "sábado":
        print("Saturday")
    case "domingo":
        print("Sunday")
    case _:
        print("Día inválido")