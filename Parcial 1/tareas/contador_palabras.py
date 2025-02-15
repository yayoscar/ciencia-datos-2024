def contador_palabras():
    print("Bienvenido al contador de palabras.")
    frase = input("Por favor, ingresa una frase: ")
    palabra = input("Ingresa la palabra que deseas contar en la frase: ")

    # Contar las apariciones de la palabra en la frase
    conteo = frase.lower().split().count(palabra.lower())

    print(f"La palabra '{palabra}' aparece {conteo} veces en la frase.")


contador_palabras()
