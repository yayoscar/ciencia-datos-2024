password = input("Ingresa tu contraseña: ")
caracteres = len(password)
if  caracteres>7:
    print("¡Buena contraseña!")
elif caracteres == 7 :
    print("La contraseña está bien, pero no es muy fuerte")
else:
    print("Tu contraseña es débil")