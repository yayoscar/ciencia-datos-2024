def clasificar_fruta(tipofruta):
    match tipofruta.lower():
        case "manzana" | "pera" | "durazno":
            print("Fruta de piel lisa.")
        case "naranja" | "limón" | "mandarina":
            print("Fruta cítrica.")
        case "sandia" | "melon":
            print("Fruta grande.")
        case _:
            print("No tengo información sobre esa fruta.")

fruta= input("Ingresa el nombre de una fruta: ")
clasificar_fruta(fruta)
