dia = input("ingresa un dia de la semana: ")
match dia.lower():
    case"lunes":
        print("monday")
    case"martes":
        print("tuesday")
    case"miercoles":
        print("Wednesday")
    case"jueves":
        print("thursday")
    case"viernes":
        print("friday")
    case"sabado":
        print("saturday")
    case"domingo":
        print("sunday")
    case _:
        print("dia no reconocido")


