while True:
    accion_usuario= input("Coloca un dia de la semana para traducir: ")
    match accion_usuario:
        case "Lunes" :
            print( )
            print("Monday")
            print( )
            print("Para salir, ingrese salir ")
        case "Martes" :
            print( )
            print("Tuesday")
            print( )
            print("Para salir, ingrese salir ")
        case "Miercoles" :
            print( )
            print("Wednesday")
            print( )
            print("Para salir, ingrese salir ")
        case "Jueves":
            print()
            print("Thursday")
            print()
            print("Para salir, ingrese salir ")
        case "Viernes":
            print()
            print("Friday")
            print()
            print("Para salir, ingrese salir ")
        case "Sabado":
            print()
            print("Saturday")
            print()
            print("Para salir, ingrese salir ")
        case "Domingo":
            print()
            print("Sunday")
            print()
            print("Para salir, ingrese salir ")
        case "salir":
            break
print("Adios")
