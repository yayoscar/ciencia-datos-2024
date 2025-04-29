frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
frase_capitalizada = "_".join(palabras_capitalizadas)
print("Frase nueva:", frase_capitalizada)