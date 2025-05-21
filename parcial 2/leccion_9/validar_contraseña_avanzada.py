password = input("ingrese una nueva contraseña")
largo = len(password)
if largo > 7:
    print("buena contraseña")
elif largo == 7:
    print("la contraseña no es muy segura")
else:
    print("la contraseña es debil")