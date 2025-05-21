
def comp_contraseña(contraseña):
    largo=False
    may=False
    num=False
    if len(contraseña) >=8:
        largo=True
    for i in range (len(contraseña)):
        if contraseña(i).isepper():
                may=True
        if contraseña(i).isnumeric():
                num=True

    if largo and may and num == True:
        return True
    else:
        return False

contraseña= input("ingrese contraseña:")
verificar=comp_contraseña(contraseña)
if verificar == True:
     print("la contraseña es segura. ")
else:
    print("la contraseña no es segura. ")