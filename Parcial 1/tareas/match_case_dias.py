dia = input("Ingresa un día de la semana: ")

match dia:
    case "Lunes" | "lunes":
        print("Monday")
    case "Martes" | "martes":
        print("Tuesday")
    case "Miercoles" | "miércoles" | "miercoles":
        print("Wednesday")
    case "Jueves" | "jueves":
        print("Thursday")
    case "Viernes" | "viernes":
        print("Friday")
    case "Sabado" | "Sábado" | "sábado" | "sabado":
        print("Saturday")
    case "Domingo" | "domingo":
        print("Sunday")
    case _:
        print("Día no reconocido")