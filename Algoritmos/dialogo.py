def conversar():
    nombre = input("Hola que tal, ¿cómo te llamas? ")
    print(f"¡Hola {nombre}! un placer conocerte.")
    print("¿como te encuentras? ")
    respuesta = input("> ")
    match respuesta:
        case "bien" | "muy bien":
         print(f"Qué bien escuchar eso,{nombre}.")
        case "mal" | "muy mal":
            print(f"eso me entristece, {nombre}.")

    print("¿Qué activdad te gusta realizar?")
    actividad = input("> ")
    print(f"¡órale! a mi igual me gusta {actividad}.")
    print("bueno, realmente fue un gusto conocerte. ¡Nos vemos pronto!")

conversar()