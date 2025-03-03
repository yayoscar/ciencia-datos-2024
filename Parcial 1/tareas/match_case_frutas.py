fruta = input("Ingresa el nombre de una fruta: ")

match fruta.lower():
    case "manzana" | "pera" | "uva":
        print("La fruta es de tipo 'Fruta de árbol'")
    case "plátano" | "mango" | "piña":
        print("La fruta es de tipo 'Fruta tropical'")
    case "fresa" | "frambuesa" | "arándano":
        print("La fruta es de tipo 'Fruta de arbusto'")
    case _:
        print("La fruta no se encuentra en nuestras categorías")