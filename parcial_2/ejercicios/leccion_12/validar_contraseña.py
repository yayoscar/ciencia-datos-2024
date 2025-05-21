def fuerza(contraseña_local):
    largo = False
    if len(contraseña_local) >8:
        largo = True
    mayus = False
    for carac in contraseña_local:
        if carac.isupper():
            mayus = True
    num = False
    for carac in contraseña_local:
        if carac.isdigit():
            num = True
    if largo and mayus and num:
        return "Contraseña fuerte"
    else:
        return "Contraseña débil"


contraseña = input("Contraseña: ")
print(fuerza(contraseña))