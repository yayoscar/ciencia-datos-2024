fruta = input("ingresa el nombre de una fruta: ")
match fruta.lower():
    case "Manzana":
        print("Es una fruta de un arbol.")
    case "mora":
        print("Es una fruta de un arbusto.")
    case "papaya":
        print("es una fruta tropical")
    case _:
        print("no conozco esa fruta")