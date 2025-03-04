fruta = input("Ingresa el nombre de la fruta:")
match fruta:

    case"manzana":
        print("manzana")
    case"pera":
        print("pera")
    case"pera":
        print("durazno")
    case"durazno":
        print("durazno")
    case"naranja":
        print("naranja")
    case"uva":
        print("uva")
    case "uva" | "fruta pequeña":
        print("uva", "fruta pequeña")
    case "mandarina" | "fruta cítrica":
        print("mandarina fruta cítrica")
    case "durazno" | "fruta de piel lisa":
        print("durazno", "fruta de piel lisa")
    case _:
        print("No conozco esa fruta")








