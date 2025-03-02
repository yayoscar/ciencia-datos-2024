def \
        clasificar_fruta(fruta):
    match fruta.lower():
        case "manzana" | "pera" | "durazno":
            print("{fruta} es una fruta de tipo pomácea.")
        case "naranja" | "limón" | "mandarina":
            print("{fruta} es una fruta cítrica.")
        case "platano" | "banana":
            print("{fruta} es una fruta tropical.")
        case "sandía" | "melon":
            print("{fruta} es una fruta de tipo cucurbitácea.")
        case _:
            print("No tengo información sobre la fruta .")

fruta = input("Ingresa el nombre de una fruta: ")
clasificar_fruta(fruta)


