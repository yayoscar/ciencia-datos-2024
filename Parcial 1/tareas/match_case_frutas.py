def identificador_frutas():
    print("Bienvenido al identificador de frutas.")
    fruta = input("Ingresa el nombre de una fruta: ").strip().lower()

    match fruta:
        case "manzana" | "pera" | "durazno":
            categoria = "Frutas de pepita"
        case "naranja" | "limón" | "mandarina":
            categoria = "Frutas cítricas"
        case "plátano" | "banana" | "guineo":
            categoria = "Frutas tropicales"
        case "fresa" | "mora" | "frambuesa":
            categoria = "Frutas del bosque"
        case _:
            categoria = "Categoría desconocida"

    print(f"La fruta '{fruta}' pertenece a la categoría: {categoria}")


identificador_frutas()


