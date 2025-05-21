contrasena = input("Ingrese contrasena:  ")
if len(contrasena) >= 8:
    print("¡Buena contraseña!")
elif len(contrasena) ==7:
    print("La contraseña está bien, pero no es muy fuerte")
else:
    print("Tu contraseña es débil.")