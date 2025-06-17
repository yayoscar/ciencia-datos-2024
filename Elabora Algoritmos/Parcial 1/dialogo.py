def conversar():
    nombre = input("Hola, ¿cómo te llamas? ")
    print(f"¡Hola {nombre}! Encantado de conocerte.")

    print("¿Qué tal estás hoy? ")
    respuesta = input("> ")
    match respuesta:
        case "bien" | "genial" | "de maravilla":
            print(f"Me alegro escuchar eso, {nombre}.")
        case "mal" | "muy mal":
            print(f"Que mal, {nombre}. :(")

    print("¿Tienes algún pasatiempo favorito? ")
    pasatiempo = input("> ")
    print(f"¡Que interesante! Me gusta {pasatiempo} tambien.")

    print(f"Bueno, {nombre}, ha sido un placer habalr contigo. ¡Hasta luego!")
conversar()