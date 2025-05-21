contraseña = input("ingrese una contraseña: ")
caracteres = len(contraseña)
if caracteres > 7:
    print("tu contraseña es segura")
else:
    print("Su contraseña es demasiad debil")