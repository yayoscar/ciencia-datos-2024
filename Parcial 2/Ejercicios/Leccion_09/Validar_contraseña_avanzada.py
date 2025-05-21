password = input("Ingrese una contraseña: ")
Largo= len(password)
if len (password) > 7:
    print("Buena contaseña!")
elif Largo == 7:
    print("La contraseña esta bien, pero no es muy fuerte")
else:
    print("La contraseña es debil")