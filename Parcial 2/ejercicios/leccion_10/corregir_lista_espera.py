try:
    lista_espera = ["juan", "maria"]
    nombre = input("Ingresa un nombre: ")
    numero = lista_espera.index(nombre)
    print(f"Es el turno de {nombre}, número {numero}")
except ValueError:
    print("zen no está en la lista")