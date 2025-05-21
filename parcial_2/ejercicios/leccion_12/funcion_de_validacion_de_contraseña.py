def fuerza(contraseña):
    largo = False
    may = False
    num = False
    if len(contraseña) >= 8:
        largo = True
    for i in range(len(contraseña)):
        if contraseña[i].isupper():
            may = True
    if contraseña[i].isnumeric():
        num = True
    if largo and may and num:
        return True
    else:
        return False
contraseña = input("Ingrese su contraseña: ")
verificar = fuerza(contraseña)
if verificar is True:
    print("Contraseña fuerte")
else:
    print("Contraseña débil")