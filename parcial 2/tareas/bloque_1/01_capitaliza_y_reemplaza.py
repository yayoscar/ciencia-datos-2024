frase = input("Escribe una frase: ")

n2 = frase.replace(" ", "_")

n3 = n2.split("_")

n4 = [n3.capitalize() for n3 in n3]

resultado = "_".join(n4)

print(resultado)