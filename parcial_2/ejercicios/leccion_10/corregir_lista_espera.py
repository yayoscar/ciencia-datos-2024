try:
    lista_espera = ['juan', 'maria']
    nombre = input("Ingresa un nombre: ")
    numero = lista_espera.index(nombre)
    print(f"El turno de {nombre} es el turno {numero + 1}")
except ValueError:
    print("El nombre no está en la lista")