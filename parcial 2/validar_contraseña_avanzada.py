contraseña = input("Ingresa una nueva contraseña: ")

longitud = len(contraseña)

if longitud > 7:
    print("¡Buena contraseña!")
elif longitud == 7:
    print("La contraseña está bien, pero no es muy fuerte")
else:
    print("Tu contraseña es débil")
