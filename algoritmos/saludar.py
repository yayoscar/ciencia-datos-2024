def conversar():
    nombre = input("Hola, ¿cuál es tu nombre? ")
    print(f"¡Hola {nombre}! Fascinado de conocerte.")
    print("Cómo estás hoy?")
    respuesta = input("> ")
    match respuesta:
       case "muy bien" | "genial" | "de maravilla":
           print(f"Me alegro de escuchar eso, {nombre}.")
       case "mal" | "muy mal":
           print(f"lol que mal, {nombre}. Espero que te sientas mucho mejor ")

    print("¿Tienes algún pasatiempo favorito?")
    pasatiempo = input("> ")
    print(f" ¡wow que interesante! igual me gusta {pasatiempo}.")

    print(f"Bueno, {nombre}, ha sido un gusto el hecho de haberte conocido y conversar. ¡hasta luego!")
conversar()



