try:
   lista_espera = ["Juan", "María"]
   nombre = input("Ingrese un nombre: ")
   numero = lista_espera.index(nombre)
   print(f"Es el turno de {nombre}, número {numero}")
except ValueError:
   print("El nombre no esta en la lista")