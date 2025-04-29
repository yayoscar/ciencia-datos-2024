día = input("Ingrese un día de la semana (en minúsculas): ")
match día:
    case"lunes":
        print("Inicio de semana")
    case "miercoles":
        print("Mitad de semana")
    case "sábado" | "domingo":
        print("Fin de semana")
    case "martes" | "jueves" | "viernes":
        print("día normal")






















