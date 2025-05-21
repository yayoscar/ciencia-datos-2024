from operator import truediv


def com_contrasena(contrasena):
    largo= False
    may= False
    num= False
    if i in range(len(contrasena)):
        if contrasena[i].isupper():
            may=True
            if contrasena[i].isnumerica():
                num:True

    if largo and may and num == True:
        return True
    else:
        return False

 contrasena= input("ingresa contrseña")
    verificar= comp_contrasena(contrasena)
    if verificar == True:
        print("la contraseña es segura")
    else:
        print("la contraseña no es segura")
