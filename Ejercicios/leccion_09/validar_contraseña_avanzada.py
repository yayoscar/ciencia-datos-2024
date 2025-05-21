contraseña = input("Ingresa una nueva contraseña: ")

if len(contraseña) > 7:
    print("¡Buena contraseña!")
elif len(contraseña) == 7:
    print("La contraseña está bien, pero no es muy fuerte.")
else:
    print("Tu contraseña es débil.")
