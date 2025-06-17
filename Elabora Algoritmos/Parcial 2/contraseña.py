def es_contraseña_segura(contraseña):
    if len(contraseña) <= 8:
        return False
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)

    return tiene_mayuscula and tiene_numero


contraseña = input("Ingresa una contraseña: ")

if es_contraseña_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña NO es segura.")