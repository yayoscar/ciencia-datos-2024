with open("historia.txt", "r") as taco:
    resultado = taco.read()
with open("historia_copia.txt", "w") as dos:
    dos.write(resultado)