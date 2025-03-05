frase = input("ingresa una frase")
palabra = input("Ingrese la palabra que desea contar")
ocurrencias = frase.lower().split().count(palabra.lower())
print(f"La palabra '{palabra}' aparece {ocurrencias} veces en la frase. ")