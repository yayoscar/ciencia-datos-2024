fruta = input("ingresa el nombre de una fruta: ")
match fruta:
    case "manzana", "pera", "durazno":
        print("esta es una fruta de tipo pomacea.")
    case "naranja", "limon", "mandarina":
        print("esta es una fruta de tipo citrica.")
    case "fresa", "cereza", "frambuesa":
        print("esta es una fruta de tipo baya.")
    case _:
        print("no se reconoce la categoria de esa fruta.")