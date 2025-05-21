def comp_contrasena(contrasena):
    largo=False
    may=False
    num=False
    if len(contrasena) >= 8:
        largo=True
    for i in range(len(contrasena)):
        if contrasena[i].isupper():
            may=True
        if contrasena[i].isnumeric():
            num = True
    if largo and may and num == True:
        return True
    else:
        return False
contrasena = input("Ingresa contraseña:  ")
verificar=comp_contrasena(contrasena)
if verificar == True:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")