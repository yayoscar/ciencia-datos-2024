frase = input()
frase = frase.replace(" ", "_")
frase = "".join(p.capitalize() for p in frase.split(""))
print(frase)