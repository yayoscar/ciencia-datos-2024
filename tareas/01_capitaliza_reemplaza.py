frase = input("ingrese una frase:")
frase_con_guiones = frase.replace("", "_")
palabras = frase_con_guiones.split("_")
palabras_capitalizadas = [palabras.capitalize() for palabras in palabras]
resultado ="_".join(palabras_capitalizadas)
print(resultado)