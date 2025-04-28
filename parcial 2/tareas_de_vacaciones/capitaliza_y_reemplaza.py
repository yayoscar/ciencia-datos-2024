frase = input()
frase = frase.replace(" ", "_")
frase = "_".join(p.capitalize() for p in frase.split("_"))
print(frase)