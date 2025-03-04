frase = input("ingrese una frase: ")

remplazo = frase.replace(" ", "_")

palabras = remplazo.split("_")
capitalizacion = [palabra.capitalize() for palabra in palabras]

frase_con_guiones= "_".join(capitalizacion)
print(frase_con_guiones)
