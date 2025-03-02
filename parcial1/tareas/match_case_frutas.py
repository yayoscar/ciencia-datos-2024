fruta = input("Ingresa el nombre de una fruta: ")
match fruta.lower():
    case "manzana" | "uvas" | "platano":
        print("Es una fruta de árbol.")
    case "fresa" | "frambuesa" | "mora":
        print("Es una fruta de arbusto.")
    case "sandía" | "melón" | "papaya":
        print("Es una fruta tropical.")
    case _:
        print("No conozco esa fruta.")