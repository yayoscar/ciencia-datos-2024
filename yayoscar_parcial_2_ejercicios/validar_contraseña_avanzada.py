password = input("ingresa una nueva contraseña:")
largo = len(password)
if largo > 7:
    print("buena contraseña")
elif largo == 7:
    print("tu contraseña esta bien solo que no es muy fuerte.")
else:
    print("tu contraseña es debil")