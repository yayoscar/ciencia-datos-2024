fruta = input("ingresa el nombre de una fruta: ")
match fruta:
    case "Manzana"|"Pera"|"Durazno":
        print("fruta de piel lisa")
    case "Naranja"|"Limon"|"Mandarina":
        print("fruta citrica")
    case "Sandia"|"Melon":
        print("fruta grande")
    case _ :
        print("Categoria desconocida")