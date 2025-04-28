# Match_case_días
Dia = input("Ingresa un día de la semana")

match Dia:
    case "Lunes" | "lunes":
        print("Monday")
    case "Martes" | "martes":
        print("Tuesday")
    case  "Miercoles" | "miercoles":
        print("Wednesday")
    case "Jueves" | "jueves":
        print("Thursday")
    case "Viernes" | "viernes":
        print("Friday")
    case "Sábado" | "sábado":
        print("Saturday")
    case "Domingo" | "domingo":
        print("Sunday")
    case "":
        print("No es un dia de la semana")




