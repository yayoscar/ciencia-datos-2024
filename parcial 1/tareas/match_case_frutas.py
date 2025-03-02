fruta = input("Ingresa el nombre de una fruta: Durazno/Pera/Manzana/Naranja/Limón/Mandarina/Sandía/Melón: ").lower()

match fruta:
    case "durazno" | "pera" | "manzana":
        print("Fruta de piel lisa")
    case "naranja" | "limón" | "mandarina":
        print("Fruta cítrica")
    case "sandía" | "melón":
        print("Fruta grande")
    case _:
        print("Categoría no identificada.")
