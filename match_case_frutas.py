fruta = input("Ingresa el nombre de una fruta: ")

match fruta:
    case "Naranja" | "LimonN" | "Mandarina":
        print("La fruta es cítrica.")
    case "Fresa" | "Cereza" | "Frambuesa":
        print("La fruta es roja.")
    case "Manzana" | "Pera" | "Melón":
        print("La fruta es verde.")
    case _:
        print("La fruta no está en la lista.")