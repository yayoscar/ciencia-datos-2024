def fuerza(contraseña):
    input("Coloque la contraseña, para verificar: " )
    largo= False
    may= False
    num= False
    if len(contrasena)>= 8:
        largo = True
    for i in range(len(contrasena)):
        if contrasena[i].isupper():
            may = True
        if contrasena[i].isumeric():
            num = True
    if largo and may and num == True :
        return True
    else:
        return False

contrasena = input("Ingrese contraseña: ")
verificar = fuerza(contrasena)
if verificar == True:
    print("Tu contraseña es segura ")
else:
    print("Tu contraseña no es segura ")