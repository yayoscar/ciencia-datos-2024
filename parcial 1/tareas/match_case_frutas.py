fruta = input("Ingresa el nombre de una fruta:")


match fruta :
    case "Manzana"|"Pera"|"Durazno":
        print("esta es una fruta de piel lisa")
    case "Naranja"|"Limón"|"Mandarina":
        print("esta es una fruta citrica")
    case "Sandia"|"Melon":
        print("esta es una futa grande")
    case _ :
        print("categoria desconocida")