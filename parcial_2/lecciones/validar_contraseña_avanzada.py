password = input("Ingrese una nueva contraseña: ")
largo = len(password)
if largo >7:
    print("¡Buena contraseña!")
elif largo == 7:
    print("La contraseña está ben, pero no es muy fuerte. ")
else:
    print("Tu contraseña es débil.")