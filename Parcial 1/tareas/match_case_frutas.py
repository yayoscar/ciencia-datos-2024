fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "Manzana" | "Pera" | "Durazno" :
        print("Fruta de piel lisa.")
    case "Naranja" | "Limón" | "Mandarina" :
        print("Fruta cítrica.")
    case "Sandia"| "Melón" :
        print("Fruta grande.")
    case " " :
        print("Categoria desconocida")