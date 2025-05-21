def contraseña (contraseña):
    largo= False
    may= False
    num= False
    if len(contraseña) >= 8:
        largo=True
    for i in range(len(contraseña)):
        if contraseña[i].isupper():
            may= True
        if contraseña[i].isummeric():
            num = True
    if largo and may and num == True:
        return True
    else:
        return False
contraseña = input("ingresa una contraseña:")
verificar = (contraseña)
if verificar == True:
    print("la contraseña:")
else:
    print("la contraseña no es segura!")