contraseña = input("Ingresa una contraseña: ")
largo = len(contraseña)
if largo > 7 :
    print("¡Buena contraseña!")
elif largo == 7:
    print("La contraseña está bien, pero no es muy fuerte")
else:
    print("Tu contraseña es débil.")