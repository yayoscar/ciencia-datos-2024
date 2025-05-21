contraseña = input("ingrese una contraseña: ")
caracteres = len(contraseña)

if caracteres > 7:
    print("su contraseña es seguraa")
elif caracteres == 7:
    print("Su contraseña es buena pero no muy segura")
else:
    print("su contraseña no es segura")
