def contra_segura(contraseña):
    largo = False
    mayus = False
    num = False
    if len(contraseña) >= 8:
        largo=True
    for i in range(len(contraseña)):
        if contraseña[i].issupper():
            num=True
        if contraseña[i].isupper():
            mayus=True
        if contraseña[i].isnumeric():
            num=True

    if largo and mayus and num == True:
        return True
    else:
        return False


contraseña= input("Ingresa contraseña:  ")
verificar=contra_segura(contraseña)
if verificar == True:
    print("La contraseña es segura")
else:
    print("La contraseña NO es segura")


