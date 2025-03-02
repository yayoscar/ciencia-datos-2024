while True:
    dia=input("ingrese un dia de la semana lunes/martes/miercoles/jueves/viernes/sabado/domingo/salir: ")
    match dia:
        case "lunes" :
             print("monday")
        case "martes":
            print("tuesday")
        case "miercoles":
            print("wednesday")
        case "jueves":
            print("thursday")
        case "viernes" :
            print("friday")
        case "sabado" :
            print("saturday")
        case "domingo" :
            print("sunday")
        case "salir" :
            print("bye")
            break