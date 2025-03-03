mensaje = "ingrese un dia de la semana: "
while True:
    dia=input("ingrese un dia de la semana Lunes/ Martes/ Miercoles/ Jueves/ Viernes/ Sabado/ Domingo: " )
    match dia:
        case "Lunes":
            print("Monday")
        case "Martes":
            print("Tuesday")
        case "Miercoles":
            print("Wednesday")
        case "Jueves":
            print("Thursday")
        case "Viernes":
            print("Friday")
        case "Sabado":
            print("Saturday")
        case "Domingo":
            print("Sunday")