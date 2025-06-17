dia = input("Ingresa un día de la semana: ")
match dia.lower():
    case "lunes":
        print("Monday")
    case "martes":
        print("Tuesday")
    case "miércoles" | "miercoles":
        print("Wednesday")
    case "jueves":
        print("Thursday")
    case "viernes":
        print("Friday")
    case "sábado" | "sabado":
        print("Saturday")
    case "domingo":
        print("Sunday")
    case _:
        print("Día no reconocido.")