fruta = input("ingresa el nombre de una fruta: ")
match fruta:
    case "manzana" | "pera" | "durazno":
        print("Esta es una fruta de tipo pomacea.")
    case "limon" | "naranja" | "mandarina":
        print("Esta es una fruta de tipo critica.")
    case "fresa" | "cereza" | "frambuesa":
        print("Esta es una fruta de tipo baya.")
    case _:
        print("no se reconoce la categoria de esta fruta.")
