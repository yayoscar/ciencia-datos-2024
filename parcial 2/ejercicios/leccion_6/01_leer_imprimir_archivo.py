frase = input("escribe una frase")
frase_con_guiones = frase.replace(" ", "_")
frase_capitalizada = "_".join([palabra.capitalize() for palabra in frase_con_guiones.split("_")])

print("resultado:", frase_capitalizada)