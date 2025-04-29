while True:
    dia =input("ingrese un dia de la semana(en minusculas): ")
    match dia:
        case "lunes":
            print("inicia la semana")
        case "miercoles":
            print("Media semana")
        case "sabado"| "domingo"| "viernes":
            print("fin de semana")
        case "martes"| "jueves":
            print("dia regular")
        case _:
            print("no es un dia valido")