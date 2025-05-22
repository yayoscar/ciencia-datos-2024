def contraseña_segura(contraseña):
    si_mayuscula = any(i.isupper() for i in contraseña)
    si_numero = any(i.isdigit() for i in contraseña)
    cantidad_valida = len(contraseña) > 8
    return si_mayuscula and si_numero and cantidad_valida
contraseña_usuario = input("ingrese su contraseña: ")
if contraseña_segura(contraseña_usuario):
    print("la contraseña cumple es muy fuerte gg")
else:
    print("la contraseña es debil zzz")