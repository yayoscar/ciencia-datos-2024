import random
while True:
    resultado = random.randint(1,2)
    if resultado == 2:
        print("Es cara")
    else:
        print("Es cruz")


    respuesta = input("Desea continuar? S/N: ")
    if respuesta == "N":
        break