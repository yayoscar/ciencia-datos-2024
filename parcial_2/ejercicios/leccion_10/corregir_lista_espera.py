lista_espera = ["juan", "maria"]
nombre = input("Ingresa un nombre: ")

if nombre in lista_espera:
    numero = lista_espera.index(nombre)
    print(f"Es el turno de {nombre}, número {numero}")
else:
    print(f"{nombre} no está en la lista")