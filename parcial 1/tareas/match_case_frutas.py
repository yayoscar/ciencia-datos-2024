fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "manzana" | "durazno" | "pera":
        print("esta fruta entra en la categoria de tipo pomacea")
    case "limon" | "mandarina" | "naranja":
        print("esta fruta entra en la categoria de tipo citrica")
    case "cereza" | "fresa" | "frambuesa":
        print("esta fruta entra en la categoria de tipo baya")
    case _:
        print("no se reconoce la categoria de esta fruta")


