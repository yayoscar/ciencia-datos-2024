fruta = input("Ingresa el nombre de una fruta: ")

match fruta.lower():
    case "manzana" | "pera" | "durazno":
        print("Fruta de piel lisa")
    case "naranja" | "limón" | "mandarina":
        print("Fruta cítrica")
    case "sandía" | "melón":
        print("Fruta grande")
    case _:
        print("Categoría desconocida")