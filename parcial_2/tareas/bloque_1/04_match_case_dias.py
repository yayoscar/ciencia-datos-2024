dia = input("Ingrese un día de la semana en minúsculas:" )
match dia:
    case "lunes":
        print("Inicio de semana")
    case "martes"|"jueves"|"viernes":
        print("Día normal")
    case "miercoles":
        print("Mitad de semana")
    case "sabado"|"domingo":
        print("Fin de semana")
        #para "Día normal", puse dos opciones
    case _:
        print("Día normal")