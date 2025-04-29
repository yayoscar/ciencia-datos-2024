def conversar():
    nombre = input("Hola, ¿cuál es tu nombre? ")
    print(f"¡Hola {nombre}! un gusto conocerte.")
    print("Cómo estás hoy?")
    respuesta = input("> ")
    match respuesta:
       case "muy bien" | "excelente" | "super bien" | "bien":
           print(f"Me da mucho gusto saberlo, {nombre}.")
       case "mal" | "muy mal" | "un poco triste":
           print(f"ay no, que mal, {nombre}. Esperomal"
                 f" que te sientas mucho mejor ")

    print("¿Tienes algún hobby?")
    hobby = input("> ")
    print(f" ¡wow que interesante! igual me gusta {hobby}, que íncreible.")

    print(f"Bueno, {nombre}, ha sido un gusto el hecho de haberte conocido y conversar. ¡hasta luego!")
conversar()






