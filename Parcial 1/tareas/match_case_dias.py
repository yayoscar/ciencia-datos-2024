
dia = input("Ingrese un día de la semana en español: ").strip().lower()

match dia:
    case "lunes":
        print("Monday")
    case "martes":
        print("Tuesday")
    case "miércoles" | "miercoles":  # Incluimos ambas opciones por la tilde
        print("Wednesday")
    case "jueves":
        print("Thursday")
    case "viernes":
        print("Friday")
    case "sábado" | "sabado":  # Consideramos ambas variantes
        print("Saturday")
    case "domingo":
        print("Sunday")
    case _:
        print("Día no válido. Intente de nuevo.")
