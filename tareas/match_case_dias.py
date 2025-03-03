
dia = input("ingrese un dia de la semana")
match dia.lower():
    case "lunes":
        print("monday")
    case "martes":
        print("Tuesday")
    case "miercoles":
        print("Wednesday")
    case "jueves":
        print("Thursday")
    case "viernes":
        print("friday")
    case "sabado":
        print("saturday")
    case "domingo":
        print("sunday")
    case _:
        print("dia no recocido.")
