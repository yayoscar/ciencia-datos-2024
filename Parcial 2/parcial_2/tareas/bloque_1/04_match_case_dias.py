dias = input("Ingresa un dia de la semana (en minuscula): ")
match dias :
    case "lunes":
        print("Inicio de semana")
    case "miercoles":
        print("Mitad de semana")
    case "sabado"|"domingo":
        print("Fin de semana")
    case "martes"|'jueves'|'viernes':
        print('Dia normal')
    case _:
        print('Mensaje no valido')