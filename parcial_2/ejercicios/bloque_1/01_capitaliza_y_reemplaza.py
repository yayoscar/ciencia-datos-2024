frase = input("Ingresa una frase: ")

frase_con_guiones = frase.replace(" ", "_")

frase_capitalizada = "".join([palabra.capitalize() for palabra in frase_con_guiones.split("")])

print("Resultado:", frase_capitalizada)