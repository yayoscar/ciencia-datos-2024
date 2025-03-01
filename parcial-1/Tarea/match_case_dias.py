def diasdelasemana (diaingles):
    match diaingles.lower():
        case "lunes":
            print(diaingles, "es monday en ingles")
        case "martes":
            print(diaingles, "es tuesday en ingles")
        case "miercoles":
            print(diaingles, "es wednesday en ingles")
        case "jueves":
            print(diaingles, "es thursday en ingles")
        case "viernes":
            print(diaingles, "es friday en ingles")
        case "sabado":
            print(diaingles, "es saturday en ingles")
        case "domingo":
            print(diaingles, "es sunday en ingles")
dia = input("Ingresa un día de la semana: ")
diasdelasemana(dia)