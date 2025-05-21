def fuerza(contraseña):
    contar = len(contraseña)
    mayus = any(letra.isupper() for letra in contraseña)
    digito = any(letra.isdigit() for letra in contraseña)
    if contar and mayus and digito:
        return "la contraseña es segura :)"
    else:
        return "la contraseña no es segura :("

usuario_contraseña = input("ingrese una contraseña: ")
print(fuerza(usuario_contraseña))