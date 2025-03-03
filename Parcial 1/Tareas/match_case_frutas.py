fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "manzana" | "pera" | "durazno":
        print("Esta es una fruta de tipo pomácea.")
    case "naranja" | "limón" | "mandarina":
        print("Esta es una fruta de tipo cítrica.")
    case "fresa" | "cereza" | "frambuesa":
        print("Esta es una fruta de tipo baya.")
    case _:
        print("No se reconoce la categoría de esta fruta.")