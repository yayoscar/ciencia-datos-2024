while True:
    dia = input("Ingresa un día de la semana (en minúsculas): ")

    if not dia.isalpha():
        print("Entrada inválida. Por favor, ingresa solo letras.")
        continue

    match dia:
        case "lunes":
            print("Inicio de semana")
            break
        case "martes":
            print("Día normal")
            break
        case "miércoles":
            print("Mitad de semana")
            break
        case "jueves":
            print("Día normal")
            break
        case "viernes":
            print("Día normal")
            break
        case "sábado" | "domingo":
            print("Fin de semana")
            break
        case _:
            print("Día inválido. Por favor, ingresa un día de la semana en minúsculas.")