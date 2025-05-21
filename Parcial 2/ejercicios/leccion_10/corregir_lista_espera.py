lista_espera = ["juan", "maria"]
nombre = input("Ingresa un nombre: ")

try:
    numero = lista_espera.index(nombre)
    print(f"Es el turno de {nombre}, número {numero}")
except ValueError:
    print(f"{nombre} no está en la lista")