def conversor_dias():
    print("Bienvenido al conversor de días.")
    dia = input("Ingresa un día de la semana en español: ").strip().lower()

    match dia:
        case "lunes":
            traduccion = "Monday"
        case "martes":
            traduccion = "Tuesday"
        case "miércoles" | "miercoles":
            traduccion = "Wednesday"
        case "jueves":
            traduccion = "Thursday"
        case "viernes":
            traduccion = "Friday"
        case "sábado" | "sabado":
            traduccion = "Saturday"
        case "domingo":
            traduccion = "Sunday"
        case _:
            traduccion = "Día no válido"

    print(f"El día '{dia}' en inglés es: {traduccion}")


conversor_dias()
