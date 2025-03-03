dia = input("Ingresa un día de la semana en español: ")
dia = dia.capitalize()
match dia:
    case "Lunes":
        print("Lunes en inglés es 'Monday'")
    case "Martes":
        print("Martes en inglés es 'Thuesday'")
    case "Miércoles"| "Miercoles":
        print("Miércoles en inglés es 'Wednesday'")
    case "Jueves":
        print("Jueves en inglés es 'Thursday'")
    case "Viernes":
        print("Viernes en inglés es 'Friday'")
    case "Sábado" | "Sabado":
        print("Sábado en inglés es 'Saturday'")
    case "Domingo":
        print("Domingo en inglés es 'Sunday'")
    case _:
        print("No es un día de la semana.")