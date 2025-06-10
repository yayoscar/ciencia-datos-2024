password = input("ingresa una nueva contraseña")
largo = len(password)
if largo > 7:
    print("buena contraseña")
elif largo == 7:
    print("la contaseña esta bien,m pero no es segura")
else:
    print("tu contraseña es mala")