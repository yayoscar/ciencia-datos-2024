frase = input("Ingrese una frase")

frase_con_guiones = frase.replace(" ", "_")

palabras = frase_con_guiones.split("_")
palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]

resultado = "_".join(palabras_capitalizadas)
print(resultado)