dias = input("Ingresa un dia de la semana:")
match dias :
    case "Lunes":
        print("En ingles es:")
        print("Monday")
    case "Martes":
        print("En ingles es:")
        print("Tuesday")
    case "Miercoles":
        print("En ingles es:")
        print("Wednesday")
    case "Jueves" :
        print("En ingles es:")
        print("Thursday")
    case "Viernes":
        print("En ingles es:")
        print("Fridat")
    case "Sabado":
        print("En ingles es:")
        print("Saturday")
    case "Domingo":
        print("En ingles es:")
        print("Sunday")
    case _:
        print("mensaje no es valido")