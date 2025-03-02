def conversar():
  nombre = input("Hola, ¿cómo te llamas? ")
  print(f"¡Hola {nombre}! Encantado de conocerte.")

  print("¿Qué tal estás hoy?")
  respuesta = input("> ")
  match respuesta:
      case "bien" | "genial" | "de maravilla":
          print(f"Me alegro escuchar eso, {nombre}.")
      case "mal" | "muy mal":
          print(f"Que mal, {nombre}. :(")

  print("¿Tienes algún pasatiempo favorito?")
  pasatiempo = input("> ")
  print(f"¡Qué interesante! Me gusta {pasatiempo} también.")

  print(f"Bueno, {nombre}, ha sido un placer hablar contigo. ¡Hasta luego!")

conversar()
