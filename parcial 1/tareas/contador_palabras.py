frase = input("Ingresa una frase: ")
palabra = input("Ingresa la palabra que deseas contar: ")
ocurrencias = frase.lower().split().count(palabra.lower())
print(f"La palabra '{palabra}' aparece {ocurrencias} veces en la frase.")
