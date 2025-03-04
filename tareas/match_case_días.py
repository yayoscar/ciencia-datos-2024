
dia = input("ingresa un día de la semana:")
match dia:
    case "Lunes" | "lunes":
        print("Monday")
    case "Martes" | "martes":
        print("Tuesday")
    case "Miercoles" | "miercoles":
        print("Wendesday")
    case "Jueves" | "jueves":
        print("Tuesday")
    case "Viernes" | "viernes":
        print("Friday")
    case "Sabado" | "sabado":
        print("Saturday")
    case"":
        print("No se reconoce el día")



