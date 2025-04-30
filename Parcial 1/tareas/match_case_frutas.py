fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "Manzana" | "Pera" | "Durazno":
        print("Fruta de piel lisa")
    case "Naranja" | "Limón" | "Mandarina":
        print("Fruta ácida")
    case "Sandía" | "Melón":
        print("Fruta grande")
    case _:
        print("Categoría desconocida")

