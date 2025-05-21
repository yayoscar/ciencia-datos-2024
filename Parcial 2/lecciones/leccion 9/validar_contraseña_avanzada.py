password = input("Ingresa una nueva contraseña: ")
largo = len(password)
if largo > 7:
    print("¡Buena conttraseña!")
elif largo == 7:
    print("la contraseña esta bien, pero no es muy fuerte")
else:
    print("¡Tu contraseña es debil!")
