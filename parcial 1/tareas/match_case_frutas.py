fruta = input("Ingresa el nombre de una fruta: ")
match fruta:
    case "sandía" |"melón"|"pepino":
        print("Esta es una fruta dulce.")
    case "coco"|"dátil"|"nuez":
        print("Esta es una fruta saludable.")
    case "maní" | "almendra" | "avellana":
        print("Esta es una fruta de tipo fruto seco.")
    case _:
        print("No se reconoce la categoría de esta fruta.")
