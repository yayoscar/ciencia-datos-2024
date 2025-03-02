fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "Manzana" | "manzana" | "Pera" | "pera" | "Durazno" | "durazno":
        print("Fruta de piel lisa")
    case "Naranja" | "naranja" | "Limon" | "limon" | "Mandarina" | "mandarina":
        print("Fruta cítrica")
    case "Sandia" | "sandia" | "Melon" | "melon":
        print("Fruta grande")
    case _ :
        print("Categoría desconocida")